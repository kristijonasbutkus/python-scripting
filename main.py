#!/usr/bin/env python

from utils.cmdParser import Parser
from connection.connectionType import ConnectionDriver
from config.configUtils import Configuration
import globals
class Program:

    def main():
        try:
            cmdParser = Parser()
            userRequestedDevice = cmdParser.getFlag('device').lower()
            globals.testDeviceModel = userRequestedDevice
            print('User selected device: {}'.format(globals.testDeviceModel))

            if cmdParser.isFlagSet('file'):
                globals.configFile = cmdParser.getFlag('file')
                print('Using user provided file path: {}'.format(cmdParser.getFlag('file')))
            else: print('Using default configuration file path {}'.format(globals.configFile))
            
            if cmdParser.isFlagSet('host'):
                globals.serialPort = cmdParser.getFlag('host')
                globals.sshHost = cmdParser.getFlag('host')

            configuration = Configuration(globals.configFile)

            if configuration.getRequestedDeviceFromConfig(configuration.configas, userRequestedDevice):
                finalDevice = configuration.getRequestedDeviceFromConfig(configuration.configas, userRequestedDevice)
            else: exit("{} device is not supported".format(globals.testDeviceModel))
        
            print('Found device {0} in config. Connection type - {1}'.format(userRequestedDevice, finalDevice.getConnectionType()))
            connection = ConnectionDriver(finalDevice.getConnectionType(), finalDevice.getModel())
            
            print('Found {} commands for device {}'.format(len(finalDevice.getCommandList()), userRequestedDevice))

            resultList = connection.execAllTestCommands(finalDevice)
            
            configuration.saveToCSV(resultList, finalDevice)

            print('Testing finished')

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    if __name__ == "__main__":
        main()