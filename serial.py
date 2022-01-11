import serial


class Serial_connection:

    def open_connection():
        try:
            ser = serial.Serial(port='/dev/ttyUSB3', baudrate=115200, timeout=0)
        except:
            print("Could not create serial connection")

    def close_connection():
            serial.close()

    def write_to_log(self, level, message, timestamp):
        data = "%s,%s,%s\n"%(str(timestamp), str(level), message)
        self.__logFile.write(data)

#log = logger()
#log.write_to_log(1, "Some text", time.time())