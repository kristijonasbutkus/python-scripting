import csv
import datetime
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

    def getRequestedDevice(self, dictionary, userSelectedDevice):
        for item in dictionary['device']:
                if item['model'] == userSelectedDevice:
                    return Device(
                        item['model'],
                        item['connection_type'],
                        item['commands'])
                    
    def saveToCSV(self, contentList, device : Device):
        try:
            filename = "%s_%s.%s" % (device.getModel(), datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S") ,"csv")
            with open ('output/{filename}'.format(filename=filename), 'a', newline='') as file:
                writer = csv.writer(file)
                for x in contentList:
                    writer.writerow(x)
            print('logging finished')
        except Exception as e:
            print(e)
    