import re
import serial
import globals

class serialConnection():

    def __init__(self):
            self.ser = serial.Serial(port='/dev/ttyUSB2', baudrate=115200, timeout=0.5)

    def close(self):
        self.close()
        
class serialUtils:

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