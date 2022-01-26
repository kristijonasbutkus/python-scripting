import argparse
import re

class Parser:
    
    __parser = None
    __flags = None
    __args = None

    def __init__(self):
        self.__parser = self.__loadParser()
        self.__flags = vars(self.__parser)
        if not self.__parser:
            raise Exception("unable to initiate parser")     

    def __loadParser(self):
        try:
            self.__parser = argparse.ArgumentParser(
                prog='modem testing with AT commands', 
                description='AT commands testing tool',
                epilog='Made by Kristijonas')
            self.__parser.add_argument('--device', help='Provide device for testing. Available devices: trm240, rutx11, rut950', required=True, action='store')
            self.__parser.add_argument('--host', help='Provide hostname for ssh/serial connection. Examples: 192.168.1.1; /dev/ttyUSB3', required=False, action='store')
            self.__parser.add_argument('--port', help='Provide port for ssh connection', required=False, action='store')
            self.__parser.add_argument('--file', help='Path to config file', required=False, action='store')
            self.__args = self.__parser.parse_args()
            return self.__args
        except:
            return None      

    def getFlag(self, flagName):
        return self.__flags[flagName]

    def isFlagSet(self, flag):
        if self.getFlag(flag):
            return True
        else: return False

