import json

class Device:
    def __init__(self, id=0, model='unknown', connection_type='unkown', commands='unkown'):
        self.id = id,
        self.model = model, 
        self.connection_type = connection_type,
        self.commands = commands

def create_device(id, model, connection_type, commands):
    return Device(id, model, connection_type, commands)

def read_json_from_file():
    try:
        with open("/home/kristijonas/Python/python-scripting/config/config.json", "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except Exception as e:
        print(e)
        
def write_to_json_file(data):
    try:
        with open("/home/kristijonas/Python/python-scripting/output/output.csv", "w") as json_file:
           return json.dumps(data, json_file, indent = 4)
    except Exception as e:
        print(e)

json_object = read_json_from_file()
#works --> json_object["device"][0]["model"] = "samsung"
print(json_object)


