#!/usr/bin/env python
import datetime
import json
import sys
from collections import namedtuple
from time import sleep
from cmd_parser import Parser
from connection_type import ConnectionDriver
from configUtils import Configuration as JsonConfig
class Program:

    def main():
        try:
            cmdParser = Parser()

            userSelectedDevice = cmdParser.getFlag()['device']
            #print(userSelectedDevice)
            print('user selected device: {}'.format(userSelectedDevice))

            configuration = JsonConfig()
            
            finalDevice = configuration.getUserRequestedDevice(configuration.configas)
            print(finalDevice)
            ###deviceCommandList = finalDevice.getCommandList()
            #deviceConnectionType = finalDevice.getConnectionType()
            commandList = finalDevice.getCommands()
            print(commandList)
            print('aaa')




            print('Found {} commands for device {}'.format(len(finalDevice.getCommandList()), userSelectedDevice))
            
            connection = ConnectionDriver(finalDevice.getConnectionType())
            #x = connection.execCommand('ATE')
            #print(type(x))
            #print(x)
            #connection.execAllCommands(finalDevice)
            

            
           
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
        

    if __name__ == "__main__":
        main()