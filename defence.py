import pynput
import os
import time
from pynput import keyboard

threshold = 0.1  # Speed Threshold
size = 3  # Size of history array
speed = 0  # Current Average Keystroke Speed
prevTime = -1  # Previous Keypress Timestamp
i = 0  # History Array Timeslot
intrusion = False  # Boolean Flag to be raised in case of intrusion detection
history = [threshold + 1] * size  # Array for keeping track of average speeds across the last n keypress


def KeyStroke(event):
    global threshold, size
    global speed, prevTime, i, history

    # Initial Condition
    if prevTime == -1:
        prevTime = time.time()
        return True

    if i >= len(history): i = 0

    # TypeSpeed = NewKeyTime - OldKeyTime
    history[i] = time.time() - prevTime
    prevTime = time.time()
    speed = sum(history) / float(len(history))
    i = i + 1

    # print("\rAverage Speed:", speed)

    # Intrusion detected
    if speed < threshold:
        print("you have been attacked, you should unplug wireless mouse/keyboard dongle")
        # keyboard = Controller()
        os.system('rundll32.exe user32.dll,LockWorkStation')


listener = keyboard.Listener(on_press=KeyStroke)
listener.start()
listener.join()
