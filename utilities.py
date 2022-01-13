import json
import re
class Utils:   

    def is_json(myjson):
        try:
            json.loads(myjson)
        except ValueError as e:
            return False
        return True

    def get_commands(self, config):
        if not self.is_json:
            return None
        return config["commands"]

    def get_model(self, config):
        if not self.is_json:
            return None
        return config["model"]

    def get_serial_response(cmd, ser):
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