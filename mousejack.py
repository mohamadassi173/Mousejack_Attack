import tkinter as tk
from tkinter import ttk
from screens import StartPage, ScannerTime, LoadingScreen


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight=1, minsize=500)
        container.grid_columnconfigure(0, weight=1, minsize=400)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage.StartPage, ScannerTime.ScannerTime, LoadingScreen.LoadingScreen):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage.StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Driver Code
app = tkinterApp()
app.mainloop()
