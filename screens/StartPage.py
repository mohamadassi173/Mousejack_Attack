import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from screens import StartPage, ScannerTime, LoadingScreen

LARGEFONT = ("Verdana", 35)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label1 = ttk.Label(self, text="STARTING MOUSEJACK ATTACK", font="Helvetica 16 bold italic")
        # label2 = ttk.Label(self, text="init crazyRadio dongle", font="Helvetica 16 bold italic")
        # putting the grid in its place by using
        # grid
        label1.place(x=200, y=25, anchor="center")
        # label2.place(x=200, y=50, anchor="center")
        progress = Progressbar(self,
                               length=100, mode='determinate')
        progress.pack(pady=10)
        progress['value'] = 20
        # self.update_idletasks()