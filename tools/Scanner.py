from __future__ import print_function, absolute_import
import time
from lib import nrf24, nrf24_reset
import mousejack
from threading import Thread
import os


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('                ' + bar, end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


# get company name by payload
# payload example: 00:C2:00:00:D1:EF:00:00:00:7E
def getCompanyName(payload):
    # logitech mouse movement packet
    if len(payload) == 10 and payload[0] == 0 and payload[1] == 194:
        return 'logitech Mouse'
    # logitech mouse movement packet
    elif len(payload) == 10 and payload[0] == 164 and payload[1] == 194:
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

    # lenovo
    elif len(payload) == 1 and payload[0] == 7:
        return "lenovo mouse or keyboard(encrypted cant attack)"

    # non-XOR encrypted Microsoft mouse
    elif len(payload) == 19 and (payload[0] == 0x08 or payload[0] == 0x0c) and payload[6] == 0x40:
        return "microsoft mouse or keyboard"

    # XOR encrypted Microsoft mouse
    elif len(payload) == 19 and payload[0] == 0x0a:
        return "microsoft mouse or keyboard"

    elif len(payload) == 6:
        return "amazon mouse or keyboard"


def scan(radio, channels, timeout):
    print()
    print()
    items = list(range(0, 5))
    # Initial call to print 0% progress
    printProgressBar(0, len(items), prefix='Please wait:', suffix='to start', length=50)

    # init the radio channel
    channel_index = 0
    radio.set_channel(channels[channel_index])

    # set timing
    dwell_time = 0.1
    last_tune = time.time()
    start_time = time.time()
    device_index = 0
    devices = {}

    # start scanning
    while time.time() - start_time < timeout:
        os.system("clear")
        print()
        print()
        print('          ##############################################################\n'
              '          #                                                            #\n'
              '          #                     MOUSEJACK ATTACK                       #\n'
              '          #                                                            #\n'
              '          ############### Scanning for available devices ##############\n')
        printProgressBar(int(time.time() - start_time), timeout)
        print()
        print()
        print("time to end: ", (int(time.time() - start_time - timeout)) * -1, "seconds")

        # change the channel
        if time.time() - last_tune > dwell_time:
            radio.set_channel(channels[channel_index])
            channel_index = (channel_index + 1) % (len(channels))
            last_tune = time.time()
        try:
            # search for payloads in specific channel
            value = radio.receive_payload()  # received packet - 23:23:45:43:13,
        except RuntimeError:
            value = []

        # if found something(payload), 5 = mac address length
        if len(value) >= 5:
            address, payload = value[0:5], value[5:]
            address.reverse()
            print(payload, address)
            devices[device_index] = []
            devices[device_index].append(address.tolist())
            devices[device_index].append(getCompanyName(payload.tolist()))
            payload = ':'.join('{:02X}'.format(x) for x in payload)
            devices[device_index].append(payload)
            device_index += 1
    devices = deleteDuplicates(devices)
    return devices


def deleteDuplicates(devices):
    temp = []
    res = dict()
    for key, val in devices.items():
        if val[0] not in temp:
            temp.append(val[0])
            res[key] = val
    return res
