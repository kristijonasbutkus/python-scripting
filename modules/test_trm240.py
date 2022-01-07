#!/usr/bin/env python

import re
from time import sleep 		#regular expressions
import serial 	#serial connection
import argparse	#cli argument parsing
import os
import subprocess
from utilities import g

sms_body = 'test text'
number = 37063841343
ctrl_z = (b'\x1A\r')
enter_key = (b'\x0D\r')
ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=0)		

def parser_check():
	parser = argparse.ArgumentParser(prog='test_trm240', description='AT command tool',
		epilog='Made by Kristijonas Butkus')
	parser.add_argument('-b', '--body',help='body of short text message (SMS)', 
		default='this is body')
	parser.add_argument('-t', '--true', help='Just to pass true or false value', 
		action='store_true')
	parser.add_argument('-f', '--file', help='Take arguments from file', nargs='*')
	args = parser.parse_args()

def get_modem_manager_status():
    return os.system("systemctl is-active --quiet ModemManager.service")

def modem_manager_action(action):
    try:
        mm_status = get_modem_manager_status()
        if action == 'stop':
            if mm_status == 0:         # 0 means service is active, 768 - inactive
                print('Stopping Modem manager service..')
                os.system("systemctl stop --quiet ModemManager.service")
            elif mm_status == 768:
                print('Modem manager service is not running. Nothing to stop.')
        elif action == 'start':
            if mm_status == 768:
                print('Starting Modem manager service..')
                os.system("systemctl start --quiet ModemManager.service")  
            elif mm_status == 0:         # 0 means service is active
                print('Modem manager service is already running.')  
        else:
            print('Unexpected action for Modem manager', action)
    except Exception as e:
        print(e)

#checks if AT command response is OK, ERROR or answer is empty
def get_at_response(cmd):
	try:
		print('Sending AT command:', cmd)
		byte_flow = b''
		ser.write(cmd)
		print('Getting AT response..')
		while True:
			one_byte = ser.read(1)
			byte_flow += one_byte
			if re.search(b"OK", byte_flow):
				print('The asnwer is OK')
				break
			elif re.search(b"ERROR", byte_flow):
				print('The asnwer is ERROR')	
				break
			elif byte_flow == b'':
				print('Could not retrieve the response (empty)')
				break
		print('Full Response was: ', byte_flow)
	except Exception as e:
		print('Exception caught: {}'.format(e))
	finally:
		print('Response check complete')

#sends SMS with provided body to provided number (without +)				
def send_sms(body, number):
	try:
		body_encoded = body.encode('ASCII')
		number_string = str(number)
		recipient = ('AT+CMGS="+{}"\r'.format(number_string)).encode('ASCII')
		print(recipient)
		ser.write(recipient)
		ser.write(enter_key)
		ser.write(body_encoded)
		ser.write(ctrl_z)
	except Exception as e:
		print(e)
	finally:
		print("SMS was sent with body:\n{}".format(body))

def get_modem_manufacturer(cmd):
	try:
		print('Sending AT command:', cmd)
		byte_flow = b''
		ser.write(cmd)
		print('Getting AT response..')
		while True:
			one_byte = ser.readline()
			byte_flow += one_byte
			if re.search(b"OK", byte_flow):
				print('The asnwer is OK')
				break
			elif re.search(b"ERROR", byte_flow):
				print('The asnwer is ERROR')	
				break
			elif byte_flow == b'':
				print('Could not retrieve the response (empty)')
				break
		print('Full Response was: ', byte_flow)
	except Exception as e:
		print('Exception caught: {}'.format(e))
	finally:
		print('Response check complete')


def main():
	#parser_check()
	#print(check_at_response(b'ATE1\r'))
	#get_at_response(b'ATE1\r')
	#ser.write(b'ATE1\r')
		#get_modem_manufacturer(b'AT+GMI\r')
	get_at_response(b'AT+GMI\r')
	#ser.write(b'AT+CMGF=1\r')
	#send_sms(sms_body, number)
	#parser_check()
	ser.close()

if __name__ == "__main__":
    main()