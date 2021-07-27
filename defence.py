from ctypes import *
import pythoncom
import pyHook
import win32clipboard
import win32ui
import os
import shutil
from time import gmtime, strftime
from sys import stdout

kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

threshold = 30  # Speed Threshold
size = 25  # Size of history array
password = "<<"
allow_auto_type_software = duckhunt.allow_auto_type_software  # Allow AutoType Software (eg. KeyPass or LastPass)
################################################################################
pcounter = 0  # Password Counter (If using password)
speed = 0  # Current Average Keystroke Speed
prevTime = -1  # Previous Keypress Timestamp
i = 0  # History Array Timeslot
intrusion = False  # Boolean Flag to be raised in case of intrusion detection
history = [threshold + 1] * size  # Array for keeping track of average speeds across the last n keypresses
randdrop = 6  # How often should one drop a letter (in Sneaky mode)
prevWindow = []  # What was the previous window
filename = "log.txt"  # Filename to save attacks


def KeyStroke(event):
    global threshold, policy, password, pcounter
    global speed, prevTime, i, history, intrusion, blacklist

    print(event.Key)
    print(event.Message)
    print("Injected", event.Injected)

    # If an intrusion was detected and we are password protecting
    # Then lockdown any keystroke and until password is entered
    if intrusion:
        print(event.Key)
        print("loool")
        if password[pcounter] == chr(event.Ascii):
            pcounter += 1;
            if pcounter == len(password):
                win32ui.MessageBox("Correct Password!", "KeyInjection Detected",
                                   4096)  # MB_SYSTEMMODAL = 4096 -- Always on top.
                intrusion = False
                pcounter = 0
        else:
            pcounter = 0

        return False

    # Initial Condition
    if prevTime == -1:
        prevTime = event.Time
        return True

    if i >= len(history): i = 0

    # TypeSpeed = NewKeyTime - OldKeyTime
    history[i] = event.Time - prevTime
    print(event.Time, "-", prevTime, "=", history[i])
    prevTime = event.Time
    speed = sum(history) / float(len(history))
    i = i + 1

    print("\rAverage Speed:", speed)

    # Intrusion detected
    if speed < threshold:
        return caught(event)
    else:
        intrusion = False
    # pass execution to next hook registered
    return True
