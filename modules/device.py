class Device:

    def __init__(self, model, connection_type, commands):
        self.model = model
        self.connection_type = connection_type
        self.commands = commands

    def getModel(self):
        return self.model

    def getConnectionType(self):
        return self.connection_type

    def getCommands(self):
        return self.commands

    def getCommandList(self):
        commandList = []
        for x in self.commands:
            commandList.append(x['command'])
        return commandList