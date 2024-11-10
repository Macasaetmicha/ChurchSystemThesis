from tkinter import *

class SideMenu:
    def __init__(self, parent, app):
        self.frame = Frame(parent, bg="#333", width=200)
        self.frame.pack(side=LEFT, fill=Y)

        title_label = Label(self.frame, text="Menu", font=("Arial", 14), bg="#333", fg="white")
        title_label.pack(pady=20)

        self.app = app  
        
        self.create_menu_button("Dashboard", command=self.go_dashboard)
        self.create_menu_button("Binyag", command=self.go_binyag)
        self.create_menu_button("Kumpil", command=self.go_kumpil)
        self.create_menu_button("Wedding", command=self.go_wedding)
        self.create_menu_button("Death", command=self.go_death)
        #self.create_menu_button("Settings", command=self.go_settings)
        #self.create_menu_button("History", command=self.go_history)
        #self.create_menu_button("Logout", command=self.logout)

    def create_menu_button(self, text, command=None):
        button = Button(self.frame, text=text, font=("Arial", 12), bg="#444", fg="white",
                        activebackground="#555", activeforeground="white", command=command)
        button.pack(fill=X, padx=10, pady=5)

    def go_dashboard(self):
        self.app.load_dashboard()

    def go_binyag(self):
        self.app.load_binyag()

    def go_kumpil(self):
        self.app.load_kumpil()

    def go_wedding(self):
        self.app.load_wedding()

    def go_death(self):
        self.app.load_death()

   