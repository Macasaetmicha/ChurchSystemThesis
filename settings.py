from tkinter import *

class Settings:
    def __init__(self, parent):
        self.frame = Frame(parent)
        label = Label(self.frame, text="Settings Content", font=("Arial", 24))
        label.pack(pady=20)

