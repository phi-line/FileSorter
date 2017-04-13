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