import re	#regular expressions
from time import sleep 		
import serial
import os

CTRL_Z = (b'\x1A\r')
ENTER_KEY = (b'\x0D\r')		
ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=0)

#checks if AT command response is OK or ERROR
def get_at_response(cmd):
	try:
		byte_flow = b''
		ser.write(cmd)
		while True:
			one_byte = ser.read(1)
			byte_flow += one_byte
			if re.search(b"OK", byte_flow):
				print('Command response is OK')
				print('Response from modem is: ', byte_flow)
				break
			elif re.search(b"ERROR", byte_flow):
				print('Command response is ERROR')
				print('Response from modem is: ', byte_flow)	
				break
	except Exception as e:
		print('Exception caught: {}'.format(e))	

def get_modem_system_info():
	try:
		byte_flow = b''
		ser.write(b'ATI\r')
		while True:
			one_byte = ser.readline()
			byte_flow += one_byte
			if re.search(b"OK", byte_flow):
				print('The asnwer is OK')
				break
			elif re.search(b"ERROR", byte_flow):
				print('The asnwer is ERROR')	
				break
		print('Full Response was: ', byte_flow)
	except Exception as e:
		print('Exception caught: {}'.format(e))