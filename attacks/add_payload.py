from __future__ import print_function, absolute_import
import time
from tools import Scanner
from lib import nrf24_reset, nrf24, payload_keys


def wait(payloads_list, time):
    for i in range(0, time * 100 + 1):
        payloads_list.append(payload_keys.payload_keys('wait'))  # keepalive


def StringPL(payloads_list, text):
    for char in text:
        payloads_list.append(payload_keys.payload_keys(char))
        payloads_list.append(payload_keys.payload_keys(''))
        payloads_list.append(payload_keys.payload_keys('wait'))


def KeyPL(payloads_list, key):
    payloads_list.append(payload_keys.payload_keys(key))
    payloads_list.append(payload_keys.payload_keys(''))
    payloads_list.append(payload_keys.payload_keys('wait'))
