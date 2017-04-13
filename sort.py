import os
import sys #args
#import glob
import shutil #hight level file operations

from exceptions import UsageError, NoSortableFiles
from extensions import Extensions as ext

def main():
    # python3 sort.py -s [PATH]
    if len(sys.argv) <= 1 or sys.argv[1] not in ['-s','-so','-d','-a']:
        raise_help()

    type = sys.argv[1]

    # python3 sort.py -a [.ext1] [.ext2] [.ext3] ...
    if type == '-a':
        e = ext()
        add_ext = [sys.argv[x] for x in range(2, len(sys.argv)) if
                   ext.is_valid(sys.argv[x])]
        if add_ext:
            e.append_ext(add_ext)
        else:
            raise_type_error(type)

    # this is only for -s, -so, and -d
    if len(sys.argv) <= 2 or not os.path.isdir(sys.argv[2]):
        raise_type_error(type)

    #python3 sort.py -so [path] [.ext1]
    if type == '-so':
        e = ext(path = sys.argv[2], single=sys.argv[3])
    else: e = ext(path = sys.argv[2])

    # {'ext': ['/path1', '/path2']}
    ext_dict = ext_dict_builder(e.ext_list)

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

def ext_dict_builder(ext_list):
    ext_dict = dict()

    for line in ext_list:
        #for file in glob.glob(''.join(path, '*', line)):
        #files = [n for n in glob('*'.join((path, line))) if os.path.isfile(n)]

        files = [f for f in os.listdir(e.path) if f.endswith(line)]
        if files:
            if line in ext_dict:
                ext_dict[line].extend(files)
            else:
                ext_dict[line] = files

    return ext_dict

def raise_help():
    message="ERROR! USAGE FORMAT MUST BE: sort.py -type"
    usage ="".join(("Types: -s (sort) | -so (sort one) | -d (display) | -a (append)\n",
                      " -s  | sort a directory\n",
                      "     | Usage: -s [path]\n",
                      "     |",
                      " -so | sort a directory for a single extension\n",
                      "     | Usage: -so [path] [.ext]\n",
                      "     |",
                      " -d  | display files that can sorted in a directory\n",
                      "     | Usage: -d [path]\n",
                      "     |",
                      " -a  | append extension(s) to the master extensions.txt\n",
                      "     | Usage: -a [.ext1] [.ext2] [.ext3] ...\n"))
    try:
        raise UsageError(message=message, usage=usage)
    except UsageError as err:
        print (err)
        raise SystemExit

def raise_type_error(type=''):
    if type not in ['-s','-so','-d','-a']:
        raise_help()
    elif type == '-s':
        try:
            raise UsageError(usage=" -s  | sort a directory\n"
                                   "     | Usage: -s [path]")
        except UsageError as err:
            print (err)
            raise SystemExit
    elif type == '-so':
        try:
            raise UsageError(usage=" -so | sort a directory for a single extension\n"
                                   "     | Usage: -so [path] [.ext]")
        except UsageError as err:
            print (err)
            raise SystemExit
    elif type == '-d':
        try:
            raise UsageError(usage=" -d  | display files that can sorted in a directory\n"
                                   "     | Usage: -d [path]")
        except UsageError as err:
            print (err)
            raise SystemExit
    elif type == '-a':
        try:
            raise UsageError(message="ERROR! NO VALID EXTENSIONS PROVIDED:",
                             usage=" -a  | append extension(s) to the master extensions.txt\n"
                                   "     | Usage: -a [.ext1] [.ext2] [.ext3] ...")
        except UsageError as err:
            print (err)
            raise SystemExit

if __name__ == '__main__':
    main()