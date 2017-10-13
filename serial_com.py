import serial_com

class serial_com():
    baud_rate = 0
    def __init__(self, baud = 9600):
        self.serial_port = serial.Serial('/dev/serial0', baud, timeout=1)
        self.serial_port.open()

    def send_recieve_Data(self, data):
        self.serial_port.write(data)
        rsp = None
        while not rsp:
            rsp = self.serial_port.read()
        return rsp
