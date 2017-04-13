import sys #args

class Extensions:
    def __init__(self, path=sys.executable, list=[]):
        self.path = path
        if not list:
            self.ext_list = Extensions.load_ext()
        else:
            self.ext_list = list

    @staticmethod
    def load_ext():
        ext_list = []
        try:
            with open('ext_list.txt') as file:
                ext_list = [l.rstrip('\n') for l in file]
        except FileNotFoundError as err:
            print("File not found error: {}".format(err))
        finally:
            return ext_list

    @staticmethod
    def append_ext(args):
        try:
            with open('ext_list.txt', 'a+') as file:
                for ext in args:
                    file.write('\n' + ext)
        except FileNotFoundError as err:
            print("File not found error: {}".format(err))

    @staticmethod
    def is_valid(ext):
        if ext.startswith("."):
            return True
        else: return False