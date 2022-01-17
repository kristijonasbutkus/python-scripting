import importlib

class Connection_type:

    __connection = None

    def __init__(self, conType):
        self.__connection = self.__load_module(conType)
        if not self.__connection:
            exit("Unable to load connection module")

    def __load_module(self, conType):
        module = None
        try:
            module = importlib.import_module('{type}'.format(type=conType))
            print('successfully loaded connection module with connection type {type}'.format(type=conType))
            return module.connection_type()
        except Exception as e:
            print(e)