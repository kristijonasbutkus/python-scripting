# python-scripting

<b>CLI tool for device testing</b>

Currently supports Teltonika TRM240 modem and RUTX11 router.

Requirements to be installed: 
> Python3 or higher
> pyserial (for serial connection)
> paramiko (for ssh connection)
> socat (for ssh command sending)

Test settings can be changed in globals.py</b>

If testing serial device, ModemManager service should be stopped or disabled on the host machine:

> systemctl stop ModemManager.service

Usage examples:
For serial device: 

<b>sudo python3 main.py -d trm240</b>

Note that sudo is needed to access serial port!

For ssh device:

<b>python3 main.py --device rutx11</b>