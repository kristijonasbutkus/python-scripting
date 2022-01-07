class Modem:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

m1 = Modem("TRM240", '192.168.1.1')

print('Modem name is {} and IP address is {}'.format(m1.name, m1.ip))