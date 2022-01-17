#!/usr/bin/env python

from collections import namedtuple
#local imports
from cmd_parser import Parsing as parser
import connection_type as ConnectionModule
from config_load import ConfigUtils as configUtils
class Program:

    def main():
        try:
            userFlags = parser.parseFlags()
            userSelectedDevice = userFlags['device']
            print('user selected device: {}'.format(userSelectedDevice))
            deviceListFromConfig = configUtils.getDevicesFromConfig(configUtils.loadJsonConfig())
            FinalDevice = configUtils.getDevice(userSelectedDevice, deviceListFromConfig)
            print(type(FinalDevice))
            print(FinalDevice)

            #contype = 'serial_1'
            #ConnectionModule.Connection_type(contype)

        except Exception as ex:
            #print(e)
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

