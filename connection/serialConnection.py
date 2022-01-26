import re
import globals
from time import sleep
import serial
from modules.device import Device
from colorama import Fore, Style

class Connection():

    __connection = None

    def __init__(self, deviceModel): 
        for model in globals.supportedSerialDeviceList:
            if not deviceModel == model:
                    exit('Device does not support serial connection. Check Json config.')
        self.__connection = self.__openConnection__()
        if not self.__connection:
            raise Exception("Unable to initialize serial connection")
        
    def __openConnection__(self):
        try:
            return serial.Serial(port=globals.serialPort, baudrate=globals.baudrate, timeout=0.5)
        except Exception as e:
            print(e) 

    def __del__(self):
        if self.__connection:
            self.__connection.close()

    def canLoad(self):
        pass

    def execAllTestCommands(self, device : Device):
        if not self.__connection:
            raise Exception("No connection")
        __successCounter = 0
        __failureCounter = 0
        __iter = 1
        __atResponse = ''
        resultList = []
        try:
            for x in device.commands:
                print('testing command {0}, expected outcome: {1}'.format(x['command'], x['expects']), "Response: ", end="")
                cmd = x['command'].encode('ASCII') + b'\r'
                self.__connection.write(cmd)
                sleep(0.5)
                tempList = []
                byte_flow = b''
                while True:
                    one_byte = self.__connection.read(1)
                    byte_flow += one_byte
                    if re.search(b"OK", byte_flow):
                        __atResponse = "OK"
                        print(Fore.GREEN + 'OK' + Style.RESET_ALL, end="\r")
                        break
                    elif re.search(b"ERROR", byte_flow):	
                        __atResponse = "ERROR"
                        print(Fore.RED + 'ERROR' + Style.RESET_ALL, end="\r")
                        break
                expected = x['expects']
                tempList.extend([__iter, x['command'], __atResponse, expected])
                __iter += 1
                if __atResponse == expected:
                    __successCounter += 1
                    tempList.append("success")  
                else:
                    __failureCounter += 1
                    tempList.append("failure")
                resultList.append(tempList)
            print('\nSuccessful commands: ' + Fore.GREEN + '{},'.format(__successCounter) + Style.RESET_ALL + ' failures: ' + Fore.RED + '{}'.format(__failureCounter) + Style.RESET_ALL)
            return resultList
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    #for testing
    def execSingleTestCommand(self, cmd):
        try:
            byte_flow = b''
            cmd = cmd.encode('ASCII') + b'\r'
            self.__connection.write(cmd)
            sleep(1)
            while True:
                one_byte = self.__connection.read(1)
                byte_flow += one_byte
                if re.search(b"OK", byte_flow):
                    return "OK"
                elif re.search(b"ERROR", byte_flow):	
                    return "ERROR"
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)