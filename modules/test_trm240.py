#!/usr/bin/env python

import re 		#regular expressions
import serial 	#serial connection
import argparse	#cli argument parsing

sms_body = 'test text'
number = 37063841343
ctrl_z = (b'\x1A\r')
enter_key = (b'\x0D\r')
ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=0.5)		

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

def parser_check():
	parser = argparse.ArgumentParser(prog='test_trm240', description='AT command tool',
		epilog='Made by Kristijonas Butkus')
	parser.add_argument('-b', '--body',help='body of short text message (SMS)', 
		default='this is body')
	parser.add_argument('-t', '--true', help='Just to pass true or false value', 
		action='store_true')
	parser.add_argument('-f', '--file', help='Take arguments from file', nargs='*')
	args = parser.parse_args()

def main():
	#parser_check()
	#print(check_at_response(b'ATE1\r'))
	get_at_response(b'ATE1\r')
	#ser.write(b'ATE1\r')
	get_at_response(b'AT+CMGF=1\r')
	#ser.write(b'AT+CMGF=1\r')
	send_sms(sms_body, number)
	#parser_check()
	ser.close()

if __name__ == "__main__":
    main()