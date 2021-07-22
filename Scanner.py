from __future__ import print_function, absolute_import

import time

import nrf24


def getCompanyName(payload):

    print(len(payload))
    # logitech mouse movement packet
    if len(payload) == 29 and payload[0] == '0' and payload[3:5] == 'C2':
        return 'logitech Mouse'

    # logitech keystroke packet
    elif len(payload) == 22 and payload[0] == 0 and payload[3:5] == 'D3':
        return 'logitech Keyboard or Mouse'

    # logitech keepalive packet
    elif len(payload) == 5 and payload[0] == 0 and payload[3:5] == '40':
        return 'logitech Keyboard or Mouse'

    # logitech sleep timer packet
    elif len(payload) == 10 and payload[0] == 0 and payload[3:5] == '4F':
        return 'logitech Keyboard or Mouse'


def scan(timeout=120.0):
    channel_index = 0
    channels = range(2, 84)
    devices = {}
    ping = [0x0f, 0x0f, 0x0f, 0x0f]
    radio = nrf24.nrf24(0)
    radio.enter_promiscuous_mode()
    radio.set_channel(channels[channel_index])
    dwell_time = 0.1
    last_tune = time.time()
    start_time = time.time()
    radio.enable_lna()
    while time.time() - start_time < timeout:
        if len(channels) > 1 and time.time() - last_tune > dwell_time:
            radio.set_channel(channels[channel_index])
            channel_index = (channel_index + 1) % (len(channels))
            last_tune = time.time()
        try:
            value = radio.receive_payload()
        except RuntimeError:
            value = []
        if len(value) >= 5:
            address, payload = value[0:5], value[5:]
            address = ':'.join('{:02X}'.format(x) for x in address)
            payload = ':'.join('{:02X}'.format(x) for x in payload)
            print("address: ", address)
            print("payload", payload)
            print("hid", getCompanyName(payload))
            devices[address] = []
            devices[address].append(address)
            devices[address].append(payload)

            devices[address].append(getCompanyName(payload))


scan()
