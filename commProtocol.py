from spi_com import *
from serial_com import *
from i2c_com import *
from usb_com import *

class commTerminal():
    protocol_status = {'SPI':['initialized':False],
                        'I2C': ['initialized': False],
                        'Serial': ['initialized': False],
                        'USB_COM': ['initialized': False]
                        }

    def __init__(self):

    #During initialization confirm that all other protocals are inactive
    def initialize_SPI(self):
        
    def initialize_I2C(self):

    def initialize_Serial(self):

    def initialize_USB_COM(self):

    #One Protocol should be active at a time
    #Confirm data parameter is valid for transmition
    #Send data with the correct protocol and wait for response
    def send_Data(self, data):
