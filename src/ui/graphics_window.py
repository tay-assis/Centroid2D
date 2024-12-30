# This file is responsible for creating the graphics window for 
# the application and its configuration.

from tkinter import *

class GraphicsWindow:
    def __init__(self, wigth, height, title):
        self.wigth = wigth
        self.height = height
        self.title = title

        self.window = Tk()
        self.window.title(self.title)
        self.window.geometry(f"{self.wigth}x{self.height}")

    def run(self):
        self.window.mainloop()