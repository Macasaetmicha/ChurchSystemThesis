# dashboard.py
from tkinter import *

class Dashboard:
    def __init__(self, parent):
        self.frame = Frame(parent)
        label = Label(self.frame, text="Dashboard Content", font=("Arial", 24))
        label.pack(pady=20)

