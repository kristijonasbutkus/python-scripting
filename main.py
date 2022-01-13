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

        except Exception as e:
            print(e)


    if __name__ == "__main__":
        main()

