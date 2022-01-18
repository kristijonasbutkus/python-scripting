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
            classifier = "{type}".format(type=conType) + "Connection"
            module = importlib.import_module('{x}'.format(x=classifier))
            return type(module.Connection())
        except Exception as e:
            print(e)
        finally:
            importlib.invalidate_caches()
            print('successfully loaded connection module with connection type {type}'.format(type=conType))

    def open(self):
        self.open()

    def close(self):
        self.close()

