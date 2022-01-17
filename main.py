#!/usr/bin/env python

from collections import namedtuple
from distutils import command
from time import sleep
#local imports
from cmd_parser import Parsing as parser
import connection_type as ConnectionModule
from config_load import ConfigUtils as configUtils
from serial1 import SerialUtils
import serial
class Program:

    def main():
        try:
            userFlags = parser.parseFlags()
            userSelectedDevice = userFlags['device']
            print('user selected device: {}'.format(userSelectedDevice))
            deviceListFromConfig = configUtils.getDevicesFromConfig(configUtils.loadJsonConfig())
            FinalDevice = configUtils.getDevice(userSelectedDevice, deviceListFromConfig)
            
            deviceCommandList = SerialUtils.getCommands(FinalDevice)
            deviceConnectionType = SerialUtils.getConnectionType(FinalDevice)
            commandCount = len(deviceCommandList)

            print('Found {} commands for device {}'.format(commandCount, userSelectedDevice))

            ser = serial.Serial(port='/dev/ttyUSB2', baudrate=115200, timeout=0.5)

            successCounter = 0
            failureCuonter = 0

            for x in deviceCommandList:
                cmd = SerialUtils.commandEncode(x['command'])
                answer = SerialUtils.testCommand(cmd, ser)
                print('cmd: {0}, answer: {1} (expected: {2})'.format(cmd, answer, x['expects']))
                if answer == x['expects']:
                    successCounter += 1
                else:
                    failureCuonter += 1
                sleep(1)
          
            print('successful commands: {0}, failures: {1}'.format(successCounter, failureCuonter))

            #contype = 'serial_1'
            #ConnectionModule.Connection_type(contype)

        except Exception as ex:
            #print(e)
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
        #finally:
        #    if ser.isOpen() == True:
        #        ser.close()
        #    else:
        #        print('Connection was never opened.')


    if __name__ == "__main__":
        main()

