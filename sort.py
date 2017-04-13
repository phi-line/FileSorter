import os
import sys #args
#import glob
import shutil #hight level file operations

class extensions:
    def __init__(self, path=sys.executable, single=''):
        self.path = path
        if not single:
            self.ext_list = extensions.load_ext()
        else:
            self.ext_list = [single]

    @staticmethod
    def load_ext():
        ext_list = []
        try:
            with open('extensions.txt') as file:
                ext_list = [l.rstrip('\n') for l in file]
        except FileNotFoundError as err:
            print("File not found error: {}".format(err))
        finally:
            return ext_list

    @staticmethod
    def append_ext(args):
        try:
            with open('extensions.txt', 'a+') as file:
                for ext in args:
                    file.write('\n' + ext)
        except FileNotFoundError as err:
            print("File not found error: {}".format(err))

class NoSortableFiles(Exception):
    def_msg = 'No known files can be sorted.'

    def __init__(self, message=def_msg):
        self.message = message

    def __str__(self):
        return self.message

def main():
    # python3 sort.py -s [PATH]
    if len(sys.argv) <= 2 and sys.argv[1] not in ['-s','-sa','-d','-a']:
        print ("Format must be sort.py -type")
        print ("Types: -s (sort) | -so (sort one) | -d (display) | -a (""append)")
        print ("Usage: -s [PATH]")
        print ("Usage: -so")
        raise SystemExit
    if sys.argv[1] == '-a':
        e = extensions()
        add_ext = [sys.argv[x] for x in range(2, len(sys.argv))]
        e.append_ext(add_ext)
        raise SystemExit
    if not os.path.isdir(sys.argv[2]):
        print ("{} is not a valid directory".format(sys.argv[2]))
        raise SystemExit

    type = sys.argv[1]

    #python3 sort.py -sa [PATH] .txt
    if type == '-so':
        e = extensions(path = sys.argv[2], single=sys.argv[3])
    else: e = extensions(path = sys.argv[2])

    # {'ext': ['/path1', '/path2']}
    ext_dict = dict()

    for ext in e.ext_list:
        #for file in glob.glob(''.join(path, '*', ext)):
        #files = [n for n in glob('*'.join((path, ext))) if os.path.isfile(n)]

        files = [f for f in os.listdir(e.path) if f.endswith(ext)]
        if files:
            if ext in ext_dict:
                ext_dict[ext].extend(files)
            else:
                ext_dict[ext] = files

    if type == '-d':
        if ext_dict:
            print(' '.join(ext_dict))
        raise SystemExit

    #for key in ext_dict make directory and move files
    elif ext_dict:
        file_count = 0
        for ext,files in ext_dict.items():
            new_dir = os.path.join(e.path, ext.replace('.', '_'))
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
            raise NoSortableFiles('No known files can be sorted.')
        except NoSortableFiles as err:
            print(err)

            raise SystemExit

if __name__ == '__main__':
    main()