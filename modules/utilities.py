#!/usr/bin/env python

import os
from time import sleep
import subprocess

#def write_to_file(row):
#	f = open('path/to/csv_file', 'w')
#	writer = csv.writer(f)
#	writer.writerow(row)
#	f.close()

modem_info = {
    "manufacturer": "",
    "model": "",
}

def get_modem_manager_status():
    return os.system("systemctl is-active --quiet ModemManager.service")

def modem_manager_action(action):
    try:
        mm_status = get_modem_manager_status()
        if action == 'stop':
            if mm_status == 0:         # 0 means service is active, 768 - inactive
                print('Stopping Modem manager service..')
                os.system("systemctl stop --quiet ModemManager.service")
            elif mm_status == 768:
                print('Modem manager service is not running. Nothing to stop.')
        elif action == 'start':
            if mm_status == 768:
                print('Starting Modem manager service..')
                os.system("systemctl start --quiet ModemManager.service")  
            elif mm_status == 0:         # 0 means service is active
                print('Modem manager service is already running.')  
        else:
            print('Unexpected action for Modem manager', action)
    except Exception as e:
        print(e)

def get_modem_information(arg):
    try:
        if get_modem_manager_status() != 0:
            modem_manager_action('stop')
        bash_string = "mmcli -m 0 | grep '{}:'".format(arg)
        output_model = subprocess.check_output(bash_string, shell=True).decode('ASCII')
        modem_model = output_model.partition(':')[2]
        return modem_model
    except Exception as e:
        print(e)

def main():
    model = get_modem_information('model')
    print(model)
    manufacturer = get_modem_information('manufacturer')
    print(manufacturer)

if __name__ == "__main__":
    main()
	
	
