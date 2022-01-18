#!/usr/bin/env python
import sys
from collections import namedtuple
from distutils import command
from time import sleep
#local imports
from cmd_parser import Parsing as parser
import connection_type as ConnectionModule
from configUtils import ConfigUtils as configUtils
from serial1 import serialUtils
import globals
import types
class Program:

    

    def main():
        try:
            userFlags = parser.parseFlags()
            userSelectedDevice = userFlags['device']
            print('user selected device: {}'.format(userSelectedDevice))
            deviceListFromConfig = configUtils.getDevicesFromConfig(configUtils.loadJsonConfig())
            FinalDevice = configUtils.getDevice(userSelectedDevice, deviceListFromConfig)
            
            deviceCommandList = configUtils.getCommands(FinalDevice)
            deviceConnectionType = configUtils.getConnectionType(FinalDevice)
            commandCount = len(deviceCommandList)

            #print('Found {} commands for device {}'.format(commandCount, userSelectedDevice))

            #ser = serial.Serial(port='/dev/ttyUSB2', baudrate=115200, timeout=0.5)
            #ConnectionModule.Connection_type(deviceConnectionType + "1")
            print('imported modules: {}'.format(sys.modules.keys))

            a = ConnectionModule.Connection_type(deviceConnectionType + "1")
            ser = a()
            print(type(ser))
            
            successCounter = 0
            failureCuonter = 0

            #for x in deviceCommandList:
            #    cmd = SerialUtils.commandEncode(x['command'])
            #    answer = SerialUtils.testCommand(cmd, serObj)
            #    print('cmd: {0}, answer: {1} (expected: {2})'.format(cmd, answer, x['expects']))
            #    if answer == x['expects']:
            #        successCounter += 1
            #    else:
            #       failureCuonter += 1
                #sleep(0.5)    # sleep is used to ensure that AT commands 
                            # have enough time to be processed
                            # disabing this option could result in errors
          
            #print('successful commands: {0}, failures: {1}'.format(successCounter, failureCuonter))

            

            #ConnectionModule.Connection_type(contype)

        except Exception as ex:
            #print(e)
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
        #finally:
        #    if serObj.isOpen() == True:
        #        serObj.close()
        #    else:
        #        print('Connection was never opened.')


    if __name__ == "__main__":
        main()


    def imports_go():
        for name, val in globals().items():
            if isinstance(val, types.ModuleType):
                yield val.__name__