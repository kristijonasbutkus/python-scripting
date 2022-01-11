#!/usr/bin/env python

import json
import csv
from time import sleep

class Device:
    
    def __init__(self, id=0, model='unknown', connection_type='unkown', commands='unkown'):
        self.id = id,
        self.model = model, 
        self.connection_type = connection_type,
        self.commands = commands

    def __str__(self, id=0, model='unknown', connection_type='unkown', commands='unkown'):
        return ("Device objektas: \n id:% s model:% s connection_type:% s commands:% s ", self.id, self.model, self.connection_type, self.commands)

    def create_device(id, model, connection_type, commands):
        return Device(id, model, connection_type, commands)

    def read_json_from_file():
        try:
            with open("/home/studentas/akademija/code/config.json", "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except Exception as e:
            print(e)
        
    def json_extract(obj, key):
        arr = []
        def extract(obj, arr, key):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr
        values = extract(obj, arr, key)
        return values

    def write_to_csv_file(row):
        try:
            with open("/home/studentas/akademija/code/output/output.csv", "w") as csv_file:
                x = json.dumps(row)
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(x)
        except Exception as e:
            print(e)

