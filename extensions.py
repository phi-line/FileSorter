import sys #args
from os.path import dirname, abspath, join

class Extensions:
    '''
    This is a class that generates a list of extensions from a master file
    It can also be passed a custom extension list instead

    Members:
    path(string) - The file path in which to target
    ext_list(list) - The list of extensions to target
    '''
    def __init__(self, path=sys.executable, list=[]):
        self.path = path
        if not list:
            self.ext_list = Extensions.load_ext()
        else:
            self.ext_list = list

    @staticmethod
    def load_ext():
        '''
        This function returns an extension list from a master file 'ext_list.txt'
        '''
        ext_list = []
        try:
            path = dirname(abspath(__file__))
            with open(join(path, 'ext_list.txt')) as file:
                ext_list = [l.rstrip('\n') for l in file]
        except FileNotFoundError as err:
            print("File not found error: {}".format(err))
        finally:
            return ext_list

    @staticmethod
    def append_ext(args):
        '''
        This function appends any number of args to the master file
        '''
        try:
            with open('ext_list.txt', 'a+') as file:
                for ext in args:
                    file.write('\n' + ext)
        except FileNotFoundError as err:
            print("File not found error: {}".format(err))

    @staticmethod
    def is_valid(ext):
        '''
        This function returns a bool whether the extension given is valid
        '''
        if ext.startswith("."):
            return True
        else: return False
