from collections import namedtuple
import json
from modules.device import Device

class Configuration:

    configas = None

    def __init__(self, config = "config.json"):
        self.__loadConfig(config)

    def __loadConfig(self, config = "config.json"):
        try:
            with open(config, "r", encoding="utf-8") as json_file:
                self.configas = json.load(json_file)
        except:
            print('Could not load json config')  

    def getUserRequestedDevice(self, dictionary : dict):
        try:
            iterator = 0
            tempCommandList = []
            #print(dictionary)
            for val in dictionary['device']:
                #print(val)
                device = Device(
                    val[iterator]['model'],
                    val[iterator]['connection_type'],
                    val[iterator]['commands']),
                iterator += 1
            return device
        except Exception as e:
            print(e) 

    