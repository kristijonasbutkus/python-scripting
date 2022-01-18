from collections import namedtuple
import json

class ConfigUtils:

    __config = None

    def __init__(self, config = "config.json"):
        self.__loadConfig(config)
        if not self.__loadConfig:
            exit("Unable to load json configuration")

    def __loadConfig(self, config):
        try:
            with open(config, "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except:
            print('Could not load json config')  

    def loadJsonConfig(config = "config.json"):
        try:
            with open(config, "r", encoding="utf-8") as jsonFile:
                return json.load(jsonFile)   
        except:
            print('Could not load json config')  

    def getDevicesFromConfig(dict):
        try:
            deviceList = []
            Device = namedtuple('Device', 'model connection_type commands')
            for x in range(len(dict['device'])):
                deviceList.append(Device(model=dict['device'][x]['model'],
                    connection_type=dict['device'][x]['connection_type'],
                    commands=dict['device'][x]['commands']
                ))
            return deviceList
        except Exception as e:
            print(e)

    def getDevice(userRequestedDeviceName, deviceList):
        devices = []
        try:
            for x in range(len(deviceList)):
                if userRequestedDeviceName == deviceList[x].model:
                    return deviceList[x]
            return None
        except Exception as e:
            print(e)

    def getCommands(Device):
        return Device.commands

    def getConnectionType(Device):
        return Device.connection_type
        
    #def saveToCSV(content):
        


