#!/usr/bin/env python
import datetime
import sys
from collections import namedtuple
from time import sleep
#local imports
from cmd_parser import Parsing as parser
import connection_type as ConnectionModule
from configUtils import ConfigUtils as configUtils
from serialConnection import Connection, serialUtils
import globals
import serial
import csv
class Program:

    def main():
        try:
            userFlags = parser.parseFlags()
            userSelectedDevice = userFlags['device']
            print('user selected device: {}'.format(userSelectedDevice))
            deviceListFromConfig = configUtils.getDevicesFromConfig(configUtils.loadJsonConfig())
            FinalDevice = configUtils.getDevice(userSelectedDevice, deviceListFromConfig)
            deviceCommandList = configUtils.getCommands(FinalDevice)
            #deviceConnectionType = configUtils.getConnectionType(FinalDevice)
            commandCount = len(deviceCommandList)
            print('Found {} commands for device {}.\nStarting tests..'.format(commandCount, userSelectedDevice))

            ser = serial.Serial(port='/dev/ttyUSB2', baudrate=115200, timeout=0.5)

            serialUtils.testAllCommands(deviceCommandList, ser, userSelectedDevice)

        
            
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
        finally:
            if ser.isOpen() == True:
                ser.close()
            else:
                print('Connection was never opened.')


    if __name__ == "__main__":
        main()