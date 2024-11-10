from tkinter import *

class Death:
    def __init__(self, parent):
        self.frame = Frame(parent)
        label = Label(self.frame, text="Death Content", font=("Arial", 24))
        label.pack(pady=20)

