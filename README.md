# Python AT command testing tool


Currently supports Teltonika TRM240 modem and RUTX11 router.

The purpose of the script is to automate AT command sending to provided host using ssh or serial port. After evaluation results are then written to a csv file.

Requirements for running the script:
```
python3 or higher
pyserial (for serial connection)
paramiko (for ssh connection)
socat (for ssh command sending)
```

Settings can be changed in <b>globals.py</b> and json configuration file config/config.json

<b>Usage examples</b>

For serial device. Atleast 1 flag 'device' has to be provided

> sudo python3 main.py --device trm240

Note that sudo is needed to access serial port. By default the port is set to /dev/ttyUSB3

For ssh device:

> python3 main.py --device rutx11

To get information about which flags can be provided enter:

> python3 main.py -h

