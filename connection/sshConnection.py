from time import sleep
import paramiko
import globals
from modules.device import Device
import re
from colorama import Fore, Style

class Connection():

    __connection = None
    __channel = None 

    def __init__(self, deviceModel):
        if not deviceModel in globals.supportedSshDeviceList:
            exit('Device does not support ssh connection. Check Json config.')
        try: 
            self.__connection = paramiko.SSHClient()
            self.__connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.__connection.connect(hostname=globals.sshHost, username=globals.sshUsername, password=globals.sshPassword, port=globals.sshPort)
            self.__channel = self.__connection.invoke_shell()
        except Exception as e:
            print(e)
        if not self.__connection and not self.__channel:
            raise Exception("Unable to initialize ssh connection")

    def __del__(self):
        if self.__connection:
            self.__connection.close()

    def execAllTestCommands(self, device : Device):
        __successCounter = 0
        __failureCounter = 0
        __iter = 1
        __atResponse = ''
        resultList = []
        if not self.__connection:
            raise Exception("No connection")
        try:
            self.__channel.send('socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\n')
            for x in device.commands:
                tempList = []
                print('testing command {0}, expected outcome: {1}'.format(x['command'], x['expects']), "Response: ", end="")
                finalCmd = (x['command'] + '\r\n').encode('ASCII')
                self.__channel.send(finalCmd)
                sleep(0.5)
                _response = self.__channel.recv(9999).decode().strip()
                if re.search("OK", _response):
                    __atResponse = "OK"
                    print(Fore.GREEN + 'OK' + Style.RESET_ALL, end="\r")
                elif re.search("ERROR", _response):
                    __atResponse = "ERROR"
                    print(Fore.RED + 'ERROR' + Style.RESET_ALL, end="\r")
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
            self.__channel.send('socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r')
            sleep(1)
            finalCmd = (cmd + '\r\n').encode('ASCII')
            print('testing single command {}'.format(finalCmd))
            self.__channel.send(finalCmd)
            sleep(1)
            _response = self.__channel.recv(9999).decode().strip()
            print(_response)
            if re.search("OK", _response):
                return "OK"
            elif re.search("ERROR", _response):
                return "ERROR"
            else:
                raise Exception("Response did not include OK or ERROR. Response was: {}".format(_response))
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)