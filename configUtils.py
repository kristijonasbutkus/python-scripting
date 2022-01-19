from collections import namedtuple
from csv import writer
import csv
import datetime
import json
import logging
import io

from modules.device import Device

class ConfigUtils:

    configas = None

    def __init__(self, config = "config.json"):
        self.__loadConfig(config)

    def __loadConfig(self, config = "config.json"):
        try:
            with open(config, "r", encoding="utf-8") as json_file:
                self.configas = json.load(json_file)
        except:
            print('Could not load json config')  

    def getDevicesFromConfig(self, config : object):
        tempList = []
        try:
            deviceList = []
            iterator = 1
            for x in config:
                print('{} iteracija'.format(iterator))
                ######## LEDGO
                device = Device(model=x[i]['model'],
                connection_type=['device'][x]['connection_type'],
                commands=['device'][x]['commands'])
                deviceList.append(device)
                iterator += iterator
            return deviceList
        except Exception as e:
            print(e) 

    #def saveToCSV(self, contentList, userSelectedDevice):
    #    return self.__connection.saveToCSV(contentList, userSelectedDevice)
    