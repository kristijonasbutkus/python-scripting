#!/usr/bin/env python

from sys import stdout
from time import sleep
from cmdParser import Parser
from connectionType import ConnectionDriver
from configUtils import Configuration as JsonConfig
import paramiko
import globals
class Program:

    def main():
        try:
            cmdParser = Parser()
            userSelectedDevice = cmdParser.getFlag()['device']
            print('user selected device: {}'.format(userSelectedDevice))

            configuration = JsonConfig()
            finalDevice = configuration.getRequestedDeviceFromConfig(configuration.configas, userSelectedDevice)
            print('Device {0} uses {1} connection'.format(userSelectedDevice, finalDevice.getConnectionType()))

            print('Found {} testing commands for device {}'.format(len(finalDevice.getCommandList()), userSelectedDevice))
            
            connection = ConnectionDriver(finalDevice.getConnectionType()) 
            resultList = connection.execAllTestCommands(finalDevice)
            
            configuration.saveToCSV(resultList, finalDevice)

            print('Device {} testing is finished'.format(finalDevice.getModel()))

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    if __name__ == "__main__":
        main()