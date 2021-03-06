import os
import sys #args
import shutil #high level file operations

from exceptions import UsageError, NoSortableFiles, Erect
from extensions import Extensions as ext

def main():
    # python3 sort.py -s [PATH]
    if len(sys.argv) <= 1 or sys.argv[1] not in ['-s','-d','-a']:
        Erect.raise_help()

    type = sys.argv[1]

    # python3 sort.py -a [.ext1] [.ext2] [.ext3] ...
    if type == '-a':
        e = ext()
        add_ext = [sys.argv[x] for x in range(2, len(sys.argv)) if
                   ext.is_valid(sys.argv[x])]
        if add_ext:
            e.append_ext(add_ext)
        else:
            Erect.raise_usage_error(type)

    # this is only for -s and -d
    if len(sys.argv) <= 2 or not os.path.isdir(sys.argv[2]):
        Erect.raise_usage_error(type)

    # python3 sort.py -s [path] [.ext1] [.ext2] [.ext3] ...
    # if no items are given it will default to the master list
    if len(sys.argv) > 3:
        ext_list = [sys.argv[x] for x in range(3, len(sys.argv)) if
                   ext.is_valid(sys.argv[x])]
        e = ext(path = sys.argv[2], list=ext_list)
    else: e = ext(path = sys.argv[2])

    # {'ext': ['/path1', '/path2']}
    ext_dict = ext_dict_builder(e)

    if type == '-d':
        if ext_dict:
            print(' '.join(ext_dict))
        raise SystemExit

    #for key in ext_dict make directory and move files
    elif ext_dict:
        file_count = 0
        for line,files in ext_dict.items():
            new_dir = os.path.join(e.path, line.replace('.', '_'))
            os.makedirs(new_dir, exist_ok=True)
            if files:
                for f in files:
                    file_count += 1
                    src_path = os.path.join(e.path, f)
                    des_path = os.path.join(new_dir, f)
                    try:
                        shutil.move(src_path, des_path)
                    except (OSError, IOError) as err:
                        #os.path.split(f)[1]
                        print ("Cannot move file {} to {}: {}".format(
                            f, des_path, err))
        print ("Sorted files into:", ' '.join(ext_dict.keys()))

    else:
        try:
            raise NoSortableFiles
        except NoSortableFiles as err:
            print(err)

            raise SystemExit

def ext_dict_builder(e):
    '''
    This function builds the extension dictionary out of the supplied
    extension object. It takes the private member ext_list and then for each
    ext type it will create a list of those files found in the src dir.
    It then fills and returns the dictionary.
    
    Arguments:
    e - an Extension object containing the path and the list of ext found

    Return:
    ext_dict - A dictionary in the format: {.ext : [ext_list]}
    '''
    ext_dict = dict()

    for line in e.ext_list:
        files = [f for f in os.listdir(e.path) if f.endswith(line)]
        if files:
            if line in ext_dict:
                ext_dict[line].extend(files)
            else:
                ext_dict[line] = files

    return ext_dict

if __name__ == '__main__':
    main()
