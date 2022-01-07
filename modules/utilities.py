#!/usr/bin/env python

import os
from time import sleep
import subprocess

#def write_to_file(row):
#	f = open('path/to/csv_file', 'w')
#	writer = csv.writer(f)
#	writer.writerow(row)
#	f.close()

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

def get_usb_modem_model():
    if get_modem_manager_status() == 0:
        #temp = os.system('mmcli -L')
        output = subprocess.check_output("mmcli -m 0 | grep 'model:'", shell=True).decode('ASCII')
        a = (output.partition(':')[2]).split()
        #arr = a.split()
        print('\n{}\n'.format(a))

def main():
    get_usb_modem_model()


if __name__ == "__main__":
    main()
	
	
