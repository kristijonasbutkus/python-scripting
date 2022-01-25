# python-scripting

<b>CLI tool for device testing. <b>

Currently supports Teltonika TRM240 modem and RUTX11 router.

Requirements to be installed: 
    Python3 
    pyserial (for serial connection)
    paramiko (for ssh connection)

Device port can be set in globals.py file

If testing serial device, ModemManager service should be stopped or disabled
If testing ssh device, following code has to be executed before:
<b>sudo socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,s3,raw,setsid,sane,echo=0,nonblock ; stty sane<b> (also requires socat installed)

Usage example for serial device: 

<b>sudo python3 main.py -d trm240<b>

Note that sudo is needed to access serial port!

Usage example for ssh device:

<b>python3 main.py --device rutx11<b>

