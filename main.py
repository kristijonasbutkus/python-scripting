#!/usr/bin/env python

from utils.cmdParser import Parser
from connection.connectionType import ConnectionDriver
from config.configUtils import Configuration as JsonConfig

import serial
import globals
class Program:

    def main():
        try:
            cmdParser = Parser()
            userSelectedDevice = cmdParser.getFlag()['device']
            print('user selected device: {}'.format(userSelectedDevice))
            configuration = JsonConfig(config="config/config.json")
            
            if configuration.getRequestedDeviceFromConfig(configuration.configas, userSelectedDevice):
                finalDevice = configuration.getRequestedDeviceFromConfig(configuration.configas, userSelectedDevice)
            else: exit("{} device is not supported".format(userSelectedDevice))
            
            print('Device {0} uses {1} connection'.format(userSelectedDevice, finalDevice.getConnectionType()))
            print('Found {} commands for device {}'.format(len(finalDevice.getCommandList()), userSelectedDevice))
            
            connection = ConnectionDriver(finalDevice.getConnectionType())
            
            resultList = connection.execAllTestCommands(finalDevice)
            
            configuration.saveToCSV(resultList, finalDevice)

            print('Device {} testing finished'.format(finalDevice.getModel()))

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    if __name__ == "__main__":
        main()