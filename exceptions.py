class NoSortableFiles(Exception):
    '''
    This is an exception raised when there are no files that can be sorted

    Members:
    message - A message that can be customized based on how it was raised
    '''
    def_msg = 'ERROR! NO KNOWN FILES CAN BE SORTED.'

    def __init__(self, message=def_msg):
        self.message = message

    def __str__(self):
        return self.message

class UsageError(Exception):
    '''
    This is an exception raised when an argument usage error occurs.

    Members:
    message - A message that can be customized based on how it was raised
    usage - A secondary message that shows the proper usage for the arg
    '''
    def_msg = 'ERROR! INVALID PATH PROVIDED:'

    def __init__(self, message=def_msg, usage=''):
        self.message = message
        self.usage = usage

    def __str__(self):
        return "\n".join((self.message,self.usage))

class Erect():
    '''
    Erect is a class that handles all types of exceptions raised when an
    invalid argument usage is given. It calls the UsageError exception and
    passes it information specific to the type of argument that was misused.
    '''
    def raise_help():
        '''
        A general help message that displays all usages possible
        '''
        message = "ERROR! USAGE FORMAT MUST BE: sort.py -type"
        usage = "".join((
                        "Types: -s (sort) | -d (display) | -a (append)\n",
                        " -s  | sort a directory\n",
                        "     | Usage: -s [path]\n",
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
        '''
        This function raises specific info based on the type arg given.
        
        Argument:
        type(string) - The type of argument
        '''
        if type not in ['-s', '-d', '-a']:
            raise_help()
        elif type == '-s':
            try:
                raise UsageError(usage=" -s  | sort a directory\n"
                                       "     | Usage: -s [path]")
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
