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
            self.__parser.add_argument('-d', '--device', help='Provide device for testing. Available devices: trm240, rutx11, rut950', required=True, action='store')
            self.__parser.add_argument('-p', '--port', help='Provide port. Example: /dev/ttyUSB2', required=False, action='store')
            self.__parser.add_argument('-f', '--file', help='Take arguments from file', required=False, action='store')
            self.__args = self.__parser.parse_args()
            return self.__args
        except:
            return None      

    def getFlags(self):
        return self.__flags

    def isPortSsh(self):
        regexIpPattern = "^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$"
        regexSerialPattern = "^/dev/+"
        if re.search(regexIpPattern ,self.getFlags()['port']):
            return True
        elif re.search(regexSerialPattern ,self.getFlags()['port']):
            return False
        else: exit("port is not recognized")

