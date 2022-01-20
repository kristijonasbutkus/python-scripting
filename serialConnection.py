import csv
import datetime
import re
from time import sleep
from urllib import response
import serial
from configUtils import Configuration
from modules.device import Device

class Connection():

    __connection = None

    def __init__(self): 
        self.__connection = self.__openConnection__()
        if not self.__connection:
            raise Exception("unable to connect")
        
    def __openConnection__(self):
        try:
            return serial.Serial(port='/dev/ttyUSB2', baudrate=115200, timeout=0.5)
        except:
            return None

    def __del__(self):
        self.__closeConnection__()

    def __closeConnection__(self):
        if self.__connection:
            self.__connection.close()

    def execCommand(self, cmd):
        if not self.__connection:
            raise Exception("No connection")
        byte_flow = b''
        cmd = cmd.encode('ASCII') + b'\r'
        self.__connection.write(cmd)
        while True:
            one_byte = self.__connection.read(1)
            byte_flow += one_byte
            if re.search(b"OK", byte_flow):
                print(byte_flow)
                return "OK"
            elif re.search(b"ERROR", byte_flow):
                print(byte_flow)	
                return "ERROR"

    def execAllCommands(self, device : Device):
        if not self.__connection:
            raise Exception("No connection")
        __successCounter = 0
        __failureCounter = 0
        __iter = 1
        __atResponse = ''
        try:
            for x in device.getCommandList():
                print('testing command {0}'.format(x))
                cmd = x['command'].encode('ASCII') + b'\r'
                self.__connection.write(cmd)
                resultList = []
                byte_flow = b''
                while True:
                    one_byte = self.__connection.read(1)
                    byte_flow += one_byte
                    if re.search(b"OK", byte_flow):
                        __atResponse = "OK"
                        break
                    elif re.search(b"ERROR", byte_flow):	
                        __atResponse = "ERROR"
                        break

                expected = x['expects']
                resultList.extend([__iter, x['command'], __atResponse, expected])
                __iter += 1
                if __atResponse == expected:
                    __successCounter += 1
                    resultList.append("success")  
                else:
                    __failureCounter += 1
                    resultList.append("failure") 
                self.saveToCSV(resultList, device.getModel)
            print('successful commands: {0}, failures: {1} Testing is finished'.format(__successCounter, __failureCounter))
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def saveToCSV(self, contentList, device : Device):
        filename = "%s_%s.%s" % (device.getModel, datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S") ,".csv")
        writer = csv.writer()
        with open ('output/{filename}'.format(filename=filename), 'a', newline='') as file:
            writer = csv.writer(file)
            for x in contentList:
                writer.writerow(x)
        