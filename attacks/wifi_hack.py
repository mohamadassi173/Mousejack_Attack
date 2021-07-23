from __future__ import print_function, absolute_import
import time
from tools import Scanner
from lib import nrf24_reset, nrf24, payload_keys


class wifi_hack:

    def __init__(self, address, radio=nrf24.nrf24(0)):
        self.radio = radio
        self.address = address
        self.payloads_list = []

    def wait(self, time):
        for i in foreach(0, time * 100 + 1):
            self.payloads_list.append(payload_keys.payload_keys('wait'))

    def addStringPayload(self, text):
        for char in text:
            self.payloads_list.append(payload_keys.payload_keys('wait'))
            self.payloads_list.append(payload_keys.payload_keys(char))
            self.payloads_list.append(payload_keys.payload_keys(''))
            self.payloads_list.append(payload_keys.payload_keys('wait'))

    def test(self):
        self.payloads_list.append(payload_keys.payload_keys('init'))
        self.payloads_list.append(payload_keys.payload_keys('wait'))
        self.payloads_list.append(self.addStringPayload("od"))
        self.payloads_list.append(payload_keys.payload_keys('wait'))
        self.payloads_list.append(payload_keys.payload_keys(''))
        self.payloads_list.append(payload_keys.payload_keys('t'))
        self.payloads_list.append(payload_keys.payload_keys('wait'))
        self.payloads_list.append(payload_keys.payload_keys(''))
        self.payloads_list.append(payload_keys.payload_keys('r'))
        self.payloads_list.append(payload_keys.payload_keys('wait'))
        self.payloads_list.append(payload_keys.payload_keys(''))
