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
            print(classifier)
            return module.Connection()
        except Exception as e:
            print(e)

    def __del__(self):
        self.__closeConnection__()

    def __closeConnection__(self):
        if self.__connection:
           del self

    def execSingleTestCommand(self, cmd):
        return self.__connection.execCommand(cmd)

    def execAllTestCommands(self, commandList):
        return self.__connection.execAllTestCommands(commandList)   

    def saveToCSV(self, contentList, device : Device):
        return self.__connection.saveToCSV(contentList, device)