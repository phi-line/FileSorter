class NoSortableFiles(Exception):
    def_msg = 'ERROR! NO KNOWN FILES CAN BE SORTED.'

    def __init__(self, message=def_msg):
        self.message = message

    def __str__(self):
        return self.message

class UsageError(Exception):
    def_msg = 'ERROR! INVALID PATH PROVIDED:'

    def __init__(self, message=def_msg, usage=''):
        self.message = message
        self.usage = usage

    def __str__(self):
        return "\n".join((self.message,self.usage))

class Erect():
    def raise_help():
        message = "ERROR! USAGE FORMAT MUST BE: sort.py -type"
        usage = "".join((
                        "Types: -s (sort) | -so (sort one) | -d (display) | -a (append)\n",
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

    def raise_usage_error(type=''):
        if type not in ['-s', '-so', '-d', '-a']:
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
                raise UsageError(
                    usage=" -so | sort a directory for a single extension\n"
                          "     | Usage: -so [path] [.ext]")
            except UsageError as err:
                print (err)
                raise SystemExit
        elif type == '-d':
            try:
                raise UsageError(
                    usage=" -d  | display files that can sorted in a directory\n"
                          "     | Usage: -d [path]")
            except UsageError as err:
                print (err)
                raise SystemExit
        elif type == '-a':
            try:
                raise UsageError(
                    message="ERROR! NO VALID EXTENSIONS PROVIDED:",
                    usage=" -a  | append extension(s) to the master extensions.txt\n"
                          "     | Usage: -a [.ext1] [.ext2] [.ext3] ...")
            except UsageError as err:
                print (err)
                raise SystemExit