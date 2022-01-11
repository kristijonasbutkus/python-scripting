#!/usr/bin/env python

import re	#regular expressions
from time import sleep 		
import serial 	#serial connection
import os

sms_body = 'test text'
number = 37063841343
ctrl_z = (b'\x1A\r')
enter_key = (b'\x0D\r')
ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=0)		


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

#checks if AT command response is OK or ERROR
def get_at_response(cmd):
	try:
		byte_flow = b''
		ser.write(cmd)
		while True:
			one_byte = ser.read(1)
			byte_flow += one_byte
			if re.search(b"OK", byte_flow):
				print('The asnwer is OK')
				print('Response from modem is: ', byte_flow)
				break
			elif re.search(b"ERROR", byte_flow):
				print('The asnwer is ERROR')
				print('Response from modem is: ', byte_flow)	
				break
	except Exception as e:
		print('Exception caught: {}'.format(e))

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

#return modem system information
def get_modem_system_info():
	try:
		yte_flow = b''
		ser.write(b'ATI\r')
		while True:
			one_byte = ser.readline()
			yte_flow += one_byte
			if re.search(b"OK", yte_flow):
				print('The asnwer is OK')
				break
			elif re.search(b"ERROR", yte_flow):
				print('The asnwer is ERROR')	
				break
		print('Full Response was: ', yte_flow)
	except Exception as e:
		print('Exception caught: {}'.format(e))
	finally:
		print('Modem system info gather completed')

def main():
	None

if __name__ == "__main__":
	main()