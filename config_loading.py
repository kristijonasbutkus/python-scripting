import json

class Config_file:

    __config = None

    def __init__(self, config = "config.json"):
        self.__loadConfig(config)
        if not self.__loadConfig:
            exit("Unable to load json configuration")

    def __loadConfig(self, config):
        try:
            with open(config, "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except:
            print('Could not load json config')  

    def load_json_config(self, config = "config.json"):
        try:
            with open(config, "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except:
            print('Could not load json config')  

    #gotta change to return dict and not LIST
    def put_devices_to_list(dict):
        device_list = []
        for x in range(len(dict['device'])):
            device_list.append(dict['device'][x])
        return device_list
