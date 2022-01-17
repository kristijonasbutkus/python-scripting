import re
import serial

class ConnectionType:

    def __init__(self):
        try:
            #serial.Serial.__init__(self)
            self.ser = serial.Serial(port='/dev/ttyUSB2', baudrate=115200, timeout=0.5)
        except:
            print("Could not create serial connection")

    def __del__(self):
        self.connection_close(serial)
        print('destructor ended program life')
        #?
    def connection_close(self):
        self.close()

class SerialUtils:

    def getCommands(Device):
        return Device.commands

    def getConnectionType(Device):
        return Device.connection_type
        
    def testCommand(cmd, ser):
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

    def commandEncode(cmd):
        if isinstance(cmd, str):
            cmd = cmd + '\r'
            return cmd.encode('ASCII')
        else:
            return None