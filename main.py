#!/usr/bin/env python

import json
from types import SimpleNamespace
import serial
from collections import namedtuple
#local imports
from utilities import Utils
from cmd_parser import Parsing as parser
import connection_type as ConnectionModule
import serial_device
from config_loading import Config_file

class Program:

    def main():
        try:
            user_flags = parser.parse_flags()
            selected_device = user_flags['device']

            python_dict = Config_file().load_json_config()
            
            device_list = Config_file.put_devices_to_list(python_dict)
            print('dfasdfas')
            for x in range(len(python_dict['device'])):
                print (device_list['device'][x])
                print('')
                #return device_list

            print(device_list)
            print('python_dict length is {}'.format(len(python_dict['device'])))

            contype = 'serial_1'
            ConnectionModule.Connection_type(contype)

        except Exception as e:
         print(e)

    if __name__ == "__main__":
        main()

