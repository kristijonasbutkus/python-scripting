import os

class Extras:

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
