from __future__ import print_function, absolute_import
import time
import nrf24

list = {
    'a': [123, 123, 1, 4, 5, 1]  # just for testing !
}


def addStringPayload(payloads_list, text):
    for char in text:
        payloads_list.append(list[char])
