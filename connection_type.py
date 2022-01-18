import importlib

class Connection_type():

    __connection = None

    def __init__(self, conType):
        self.__connection = self.__load_module(conType)
        if not self.__connection:
            exit("Unable to load connection module {}".format(conType))

    def __load_module(self, conType):
        module = None
        try:
            classifier = "{type}".format(type=conType[:-1]) + "Connection"
            module = importlib.import_module('{x}'.format(x=classifier))
            
            print(classifier)
            return module.Connection()
            print('successfully loaded connection module with connection type {type}'.format(type=conType))
        except Exception as e:
            print(e)

    def close(self):
        self.close()