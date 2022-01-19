import re
from time import sleep
from urllib import response
import serial
from configUtils import ConfigUtils

class Connection():

    __connection = None

    def __init__(self): 
        self.__connection = self.__openConnection__()
        if not self.__connection:
            raise Exception("unable to connect")
        
    def __openConnection__(self):
        ser = None
        try:
            return serial.Serial(port='/dev/ttyUSB2', baudrate=115200, timeout=.5)
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

    def execAllCommandsInList(self, commandList):
        if not self.__connection:
            raise Exception("No connection")
        __successCounter = 0
        __failureCounter = 0
        __iter = 1
        __atResponse = b''

        try:
            for x in commandList:
                cmd = x['command'].encode('ASCII') + b'\r'
                self.__connection.write(cmd)
                __resultList = []
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
                __resultList.extend([__iter, x['command'], __atResponse, expected])
                __iter += 1
                if __atResponse == expected:
                    __successCounter += 1
                    __resultList.append("success")  
                else:
                    __failureCounter += 1
                    __resultList.append("failure") 
                #saveToCSV(resultList, userSelectedDevice)
                print('successful commands: {0}, failures: {1}\n'.format(__successCounter, __failureCounter))
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

