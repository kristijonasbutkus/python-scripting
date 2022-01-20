import importlib

from modules.device import Device

class ConnectionDriver():

    __connection = None

    def __init__(self, conType):
        self.__connection = self.__load_module(conType)
        if not self.__connection:
            raise Exception("Unable to load connection module {}".format(conType))

    def __load_module(self, conType):
        module = None
        try:
            classifier = "{type}".format(type=conType) + "Connection"
            module = importlib.import_module('{x}'.format(x=classifier))
            return module.Connection()
        except Exception as e:
            print(e)
        #finally:
        #    print('successfully loaded connection module with connection type {type}'.format(type=conType))

    def __del__(self):
        self.__connection.__closeConnection__()

    def __closeConnection__(self):
        if self.__connection:
           del self

    def execCommand(self, cmd):
        return self.__connection.execCommand(cmd)

    def execAllCommands(self, commandList):
        return self.__connection.execAllCommandsInList(commandList)   

    def saveToCSV(self, contentList, device : Device):
        return self.__connection.saveToCSV(contentList, device)