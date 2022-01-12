import argparse

class Parsing:

    def __init__(self):
        self.parse_flags()      

    def parse_flags():
        parser = argparse.ArgumentParser(prog='modem testing', description='AT commands testing tool',
            epilog='Made by Kristijonas Butkus')
        parser.add_argument('-d', '--device', help='Provide device for testing. TRM240, RUTX11, RUT950', required=True, action='store')
        parser.add_argument('-f', '--file', help='Take arguments from file', action='store')
        args = parser.parse_args()
        return vars(args)