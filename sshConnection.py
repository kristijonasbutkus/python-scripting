class sshConnection:
        #ssh connection is not configured yet.
    def __init__(self): 
        self.__connection = self.__openConnection__()
        if not self.__connection:
            raise Exception("unable to establish ssh connection")
  
    def __openConnection__(self):
        try:
            pass
        except:
            return None

    def __del__(self):
        self.__closeConnection__()

    def __closeConnection__(self):
        if self.__connection:
            self.__connection.close()