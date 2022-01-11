#!/usr/bin/env python

import re
import serial
import os
import argparse
import sys
from utilities import Device
import device_trm240
class Test:
        
    def parser_check():
        parser = argparse.ArgumentParser(prog='modem testing', description='AT commands testing tool',
            epilog='Made by Kristijonas Butkus')
        parser.add_argument('-d', '--device', help='Provide device for testing. TRM240, RUTX11, RUT950', required=True, action='store')
        parser.add_argument('-f', '--file', help='Take arguments from file', action='store')
        args = parser.parse_args()
        return vars(args)

    def get_selected_device(device : Device):
        selected_modem = device.get("device")
        print('Selected testing device is {}.'.format(selected_modem))
        return selected_modem


    def run_commands(tests, device):
        for i in range(len(tests)):
            print('Testing command {}'.format(i+1))
            cmd = (tests[i]+"\r").encode('ASCII')
            device.get_at_response(cmd, serial)
    
    #def get_connection_type(selected_device): #after reading from JSON file
     #   fromfile = Device.read_json_from_file()
      #  ###

    try:
        user_options = parser_check()
        print(user_options)
        selected_device = get_selected_device(user_options)
        print(type(selected_device))

        ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=0.5)	
        fromfile = Device.read_json_from_file()
        modem = Device.json_extract(fromfile, selected_device)
    except Exception as e:
        print(e)
