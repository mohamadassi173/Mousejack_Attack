from __future__ import print_function, absolute_import

import time

import nrf24


def getCompanyName(payload):

    # logitech mouse movement packet
    if len(payload) == 10 and payload[0] == '0' and payload[1] == 0xC2:
        return 'logitech Mouse'

    # logitech keystroke packet
    elif len(payload) == 22 and payload[0] == 0 and payload[1] == 0xD3:
        return 'logitech Keyboard or Mouse'

    # logitech keepalive packet
    elif len(payload) == 5 and payload[0] == 0 and payload[1] == 0x40:
        return 'logitech Keyboard or Mouse'

    # logitech sleep timer packet
    elif len(payload) == 10 and payload[0] == 0 and payload[1] == 0x4F:
        return 'logitech Keyboard or Mouse'

    # non-XOR encrypted Microsoft mouse
    elif len(payload) == 19 and (payload[0] == 0x08 or payload[0] == 0x0c) and payload[6] == 0x40:
        return "microsoft mouse or keyboard"

    # XOR encrypted Microsoft mouse
    elif len(payload) == 19 and payload[0] == 0x0a:
        return "microsoft mouse or keyboard"

    elif len(payload) == 6:
        return "amazon mouse or keyboard"

radio = nrf24.nrf24(0)
def scan(timeout=10):

    # init the radio
    channel_index = 0
    channels = range(2, 84)
    devices = {}
    radio.enter_promiscuous_mode()
    radio.set_channel(channels[channel_index])

    # set timing
    dwell_time = 0.1
    last_tune = time.time()
    start_time = time.time()
    radio.enable_lna()

    # start scanning
    while time.time() - start_time < timeout:

        # change the channel
        if time.time() - last_tune > dwell_time:
            radio.set_channel(channels[channel_index])
            channel_index = (channel_index + 1) % (len(channels))
            last_tune = time.time()
        try:
            # search for payloads in specific channel
            value = radio.receive_payload()
        except RuntimeError:
            value = []

        # if found something(payload), 5 = mac address length
        if len(value) >= 5:
            address, payload = value[0:5], value[5:]
            address.reverse()
            address = ':'.join('{:02X}'.format(x) for x in address)
            payload = ':'.join('{:02X}'.format(x) for x in payload)
            devices[address] = []
            devices[address].append(address)
            devices[address].append(payload)
            devices[address].append(getCompanyName(payload))
    return devices

scan()
