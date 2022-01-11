#!/usr/bin/env python

import serial
import os
import argparse
import sys
import importlib
from config_utilities import Device
import device_trm240


class Test:
        
    def parser_check():
        parser = argparse.ArgumentParser(prog='test_trm240', description='AT commands testing tool',
            epilog='Made by Kristijonas Butkus')
        parser.add_argument('-f', '--file', help='Take arguments from file', nargs='*')
        parser.add_argument('-d', '--device', help='Provide device for testing. TRM240, RUTX11, RUT950')
        args = parser.parse_args()

    parser_check()
    ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=0)	
    fromfile = Device.read_json_from_file()
    command_values = Device.json_extract(fromfile, 'command')

    print('Testing trm240 modem.')
    
    cmd = (command_values[0]+"\r").encode('ASCII')
    print('command 1-----------------')
    device_trm240.get_at_response(cmd)
    print('command 2-----------------')
    device_trm240.get_modem_system_info()
    cmd = (command_values[1]+"\r").encode('ASCII')
    device_trm240.get_at_response(cmd)
    device_trm240.ser.close()