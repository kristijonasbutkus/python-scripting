#!/usr/bin/env python

import sys
import os
import re
import serial
import time
import codecs

sms_body = sys.argv[1]
ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=1)
ctrl_z = (b'\x1A\r')
enter_key = (b'0D\r')
			
def send_at_command(cmd):
	try:
		ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=1)
		byte_flow = b''	
		ser.write(cmd)
		while True:
			new_char = ser.read(1)
			byte_flow += new_char
			if (len(byte_flow)>=4)and(byte_flow[-4:])==(b'\r\nOK'):
				print("The asnwer is OK for command", cmd)
				break
			elif len(byte_flow) >= 7 and byte_flow[-7:] == b'\r\nERROR':
				print('The asnwer is ERROR for command', cmd)	
				break
	except Exception as e:
		print(e)
	finally:
		print("Command sent successfully")
		ser.close()
	
					
def send_sms_command(body):
	try:
		ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=0.5)
		ser.write(b'AT+CMGS="+37063841343"\r')
		ser.write(enter_key)
		final_body = body.encode('ASCII')
		ser.write(final_body)
		ser.write(ctrl_z)
	except Exception as e:
		print(e)
	finally:
		print("SMS was sent. closing connestion..")
		ser.close()
		
def main():
	send_at_command(b'ATE1\r')
	send_at_command(b'AT+CMGF=1\r')
	send_sms_command(sms_body)
    		
if __name__ == "__main__":
    main()
	
	
