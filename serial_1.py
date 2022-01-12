import serial
import re

class connection_type:

    def __init__(self):
        try:
            ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=0)
        except:
            print("Could not create serial connection")
        finally:
            print('serial connection established.')

    #def __del__(self):
        #self.connection_close(serial)
     #   print('destructor ended program life')

    def connection_close():
        pass

    def get_serial_response(cmd, ser : serial):
        try:
            byte_flow = b''
            ser.write(cmd)
            while True:
                one_byte = ser.read(1)
                byte_flow += one_byte
                if re.search(b"OK", byte_flow):
                    print('Command response is OK')
                    print('Response from modem is: ', byte_flow)
                    break
                elif re.search(b"ERROR", byte_flow):
                    print('Command response is ERROR')
                    print('Response from modem is: ', byte_flow)	
                    break
        except Exception as e:
            print('Exception caught: {}'.format(e))