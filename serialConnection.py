import re
from tokenize import String
import serial
from configUtils import ConfigUtils
import globals

class Connection():

    __connection = None

    def __init__(self, port='/dev/ttyUSB2', baudrate=115200, timeout=.5): 
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.open(self.port, self.baudrate, self.timeout)

        #open(port,baudrate,timeout)
    def open(port, baudrate, timeout):
        return serial.Serial(port, baudrate, timeout)

    def open(self):
        self.open()

    def close(self):
        self.close()

    #def __init__(self, port, baudrate, timeout):
    ##    self.port = port
     #   self.baudrate = baudrate
     #   self.timeout = timeout    
     #   self.__connection = self.connect(self.port, self.baudrate, self.timeout)
        #self.ser = serial.Serial(port='/dev/ttyUSB2', baudrate=115200, timeout=0.5)

        
class serialUtils:



    def testSingleCommand(cmd, ser):
        try:
            byte_flow = b''
            ser.write(cmd)
            while True:
                one_byte = ser.read(1)
                byte_flow += one_byte
                if re.search(b"OK", byte_flow):
                    return "OK"
                elif re.search(b"ERROR", byte_flow):	
                    return "ERROR"
        except Exception as e:
            print('Exception caught: {}'.format(e))

    def testAllCommands(deviceCommandList, ser : serial, userSelectedDevice):
        successCounter = 0
        failureCounter = 0
        iter = 1
        __configUtils = ConfigUtils
        try:
            finalList = []
            for x in deviceCommandList:

                resultList = []
                cmd = serialUtils.commandEncode(x['command'])
                response = serialUtils.testSingleCommand(cmd, ser)
                expected = x['expects']
                resultList.extend([iter, x['command'], response, expected])
                iter += 1
                if response == expected:
                    successCounter += 1
                    resultList.append("success")  
                else:
                    failureCounter += 1
                    resultList.append("failure") 
                print(resultList)
                __configUtils.saveToCSV(resultList, userSelectedDevice)
            
            print('successful commands: {0}, failures: {1}\n'.format(successCounter, failureCounter))
        except Exception as e:
            print(e)

    def commandEncode(cmd):
        if isinstance(cmd, str):
            cmd = cmd + '\r'
            return cmd.encode('ASCII')
        else:
            return None