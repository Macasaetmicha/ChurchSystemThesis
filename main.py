from tkinter import *
from side_menu import SideMenu
from dashboard import Dashboard
from binyag import Binyag
from kumpil import Kumpil
from wedding import Wedding
from death import Death
from settings import Settings
from history import History


class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Dashboard")
        self.root.state("zoomed")

        self.sidebar = SideMenu(self.root, self)  # Sidebar with navigation
        self.sidebar.frame.pack(side=LEFT, fill=Y)

        # Initially load the Dashboard
        self.dashboard = Dashboard(self.root)
        self.dashboard.frame.pack(side=RIGHT, fill=BOTH, expand=True)

    # Methods to load the content for each page (Dashboard, Binyag, Kumpil, etc.)
    def load_dashboard(self):
        self.clear_screen()
        self.sidebar = SideMenu(self.root, self)  # Sidebar with navigation
        self.sidebar.frame.pack(side=LEFT, fill=Y)
        self.dashboard = Dashboard(self.root)
        self.dashboard.frame.pack(side=RIGHT, fill=BOTH, expand=True)

    def load_binyag(self):
        self.clear_screen()
        self.sidebar = SideMenu(self.root, self)  # Sidebar with navigation
        self.sidebar.frame.pack(side=LEFT, fill=Y)
        self.binyag = Binyag(self.root)
        self.binyag.frame.pack(side=RIGHT, fill=BOTH, expand=True)

    def load_kumpil(self):
        self.clear_screen()
        self.sidebar = SideMenu(self.root, self)  # Sidebar with navigation
        self.sidebar.frame.pack(side=LEFT, fill=Y)
        self.kumpil = Kumpil(self.root)
        self.kumpil.frame.pack(side=RIGHT, fill=BOTH, expand=True)

    def load_wedding(self):
        self.clear_screen()
        self.sidebar = SideMenu(self.root, self)  # Sidebar with navigation
        self.sidebar.frame.pack(side=LEFT, fill=Y)
        self.wedding = Wedding(self.root)
        self.wedding.frame.pack(side=RIGHT, fill=BOTH, expand=True)

    def load_death(self):
        self.clear_screen()
        self.sidebar = SideMenu(self.root, self)  # Sidebar with navigation
        self.sidebar.frame.pack(side=LEFT, fill=Y)
        self.death = Death(self.root)
        self.death.frame.pack(side=RIGHT, fill=BOTH, expand=True)

    def load_settings(self):
        self.clear_screen()
        self.sidebar = SideMenu(self.root, self)  # Sidebar with navigation
        self.sidebar.frame.pack(side=LEFT, fill=Y)
        self.settings = Settings(self.root)
        self.settings.frame.pack(side=RIGHT, fill=BOTH, expand=True)

    def load_history(self):
        self.clear_screen()
        self.sidebar = SideMenu(self.root, self)  # Sidebar with navigation
        self.sidebar.frame.pack(side=LEFT, fill=Y)
        self.history = History(self.root)
        self.history.frame.pack(side=RIGHT, fill=BOTH, expand=True)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()  

