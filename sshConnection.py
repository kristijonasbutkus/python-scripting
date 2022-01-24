from time import sleep
import paramiko
import globals
from modules.device import Device
import re

class Connection():

    __connection = None
    __channel = None 

    def __init__(self):
        self.__connection = paramiko.SSHClient()
        self.__connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__connection.connect(hostname=globals.sshHost, username=globals.sshUsername, password=globals.sshPassword)
        self.__channel = self.__connection.invoke_shell()
        if not self.__connection and not self.__channel:
            raise Exception("could not create ssh connection")

    def __del__(self):
        if self.__connection:
            self.__connection.close()
        raise Exception("SSH conenction is not open")

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
                raise Exception("Regex found nothing")
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def execAllTestCommands(self, device : Device):
        __successCounter = 0
        __failureCounter = 0
        __iter = 1
        __atResponse = ''
        resultList = []
        if not self.__connection:
            raise Exception("No connection")
        try:
            self.__channel.send('socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r')
            for x in device.commands:
                tempList = []
                print('testing command {}'.format(x['command']))
                finalCmd = (x['command'] + '\r\n').encode('ASCII')
                self.__channel.send(finalCmd)
                sleep(0.5)
                _response = self.__channel.recv(9999).decode().strip()
                if re.search("OK", _response):
                    __atResponse = "OK"
                elif re.search("ERROR", _response):
                    __atResponse = "ERROR"
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
            print('successful commands: {0}, failures: {1} Testing is finished'.format(__successCounter, __failureCounter))
            return resultList

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)