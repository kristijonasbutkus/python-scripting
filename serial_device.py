import re	#regular expressions
from time import sleep 		
import serial
import os


ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=0)

class Serial_device:

	def __init__(self, model, connection_type, commands):
		self.model = model
		self.connection_type = connection_type
		self.commands = commands




	
