#!/usr/bin/env python
import datetime
import json
import sys
from collections import namedtuple
from time import sleep
from cmd_parser import Parsing as parser
import connection_type as ConnectionModule
from configUtils import ConfigUtils as configUtils
from modules.device import Device
class Program:

    def main():
        try:
            
            userFlags = parser.parseFlags()
            userSelectedDevice = userFlags['device']
            print('user selected device: {}'.format(userSelectedDevice))
            
            config = configUtils()

            print(config.configas)
            list = config.getDevicesFromConfig(config.configas)
            print(list)




            #with open("config.json", "r", encoding="utf-8") as json_file:
               # __config = json.load(json_file)

            #print(config)

            #device1 = Device("device", "trm240", 'serial', 'commandz')
           # config.getDevicesFromConfig
            #a = config.getDevicesFromConfig(config)
            #print(a)

            #deviceListFromConfig = config.getDevicesFromConfig(config)


            #print(deviceListFromConfig)
            #FinalDevice = configUtils.getDevice(userSelectedDevice, deviceListFromConfig2)
            #print(FinalDevice)
            #FinalDevice2 = Device()
            #deviceCommandList = configUtils.getCommands(FinalDevice)
            #deviceConnectionType = configUtils.getConnectionType(FinalDevice)
            #commandCount = len(deviceCommandList)
            #print('Found {} commands for device {}'.format(commandCount, userSelectedDevice))
            #print(deviceCommandList)
            

            
            #connection = ConnectionModule.Connection_type(deviceConnectionType)
            #x = connection.execCommand('AT+CIMI=!')
            #print(x)
            #connection.execAllCommandsInList(deviceCommandList)
            

            
           
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
        

    if __name__ == "__main__":
        main()