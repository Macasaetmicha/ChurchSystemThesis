from tkinter import *
from PIL import Image, ImageTk
from main import MainPage

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")

        # Maximize window
        self.root.state("zoomed")
        
        # Loads background image
        try:
            image = Image.open("Images/background1.png")
            self.bg = ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print("Background image not found.")
            self.bg = None
        
        # Display background image
        if self.bg:
            self.bg_image = Label(self.root, image=self.bg)
            self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame (half for logo, half for login form)
        self.Frame_login = Frame(self.root, bg="#e5f1de")
        self.Frame_login.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.65, relheight=0.5)

        # Left side: Company Logo
        try:
            logo_image = Image.open("Images/logIn.png").resize((200, 200))
            self.logo = ImageTk.PhotoImage(logo_image)
        except FileNotFoundError:
            print("Logo image not found.")
            self.logo = None
        
        # Display logo on the left side of the login frame
        if self.logo:
            self.logo_label = Label(self.Frame_login, image=self.logo, bg="#e5f1de")
            self.logo_label.place(relx=0.4, rely=0.5, anchor="e", relwidth=0.4, relheight=1)

        # Right side: Email & Password fields and Login button
        self.form_frame = Frame(self.Frame_login, bg="white")
        self.form_frame.place(relx=0.4, rely=0.5, anchor="w", relwidth=0.6, relheight=1)

        inner_frame = Frame(self.form_frame, bg="white")
        inner_frame.pack(expand=True) 

        # Username Label and Entry
        username_label = Label(inner_frame, text="Username", font=("Arial", 12), fg="black", bg="white", anchor="w", justify="left")
        username_label.pack(pady=(10, 2), padx=(10, 10), fill="x")

        self.username_entry = Entry(inner_frame, font=("Arial", 12), bg="lightgray", bd=0, width=50)
        self.username_entry.pack(ipady=8, pady=5, padx=(10, 10), fill="x")

        # Password Label and Entry
        password_label = Label(inner_frame, text="Password", font=("Arial", 12), fg="black", bg="white", anchor="w", justify="left")
        password_label.pack(pady=(10, 2), padx=(10, 10), fill="x")

        self.password_entry = Entry(inner_frame, font=("Arial", 12), bg="lightgray", bd=0, show="*", width=50)
        self.password_entry.pack(ipady=8, pady=5, padx=(10, 10), fill="x")

        # Login Button
        login_button = Button(inner_frame, text="Login", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=self.login, relief="flat", bd=0)
        login_button.pack(pady=20, padx=(10, 10), fill="x")
        
        # Feedback Label
        self.feedback_label = Label(inner_frame, text="", font=("Arial", 12), fg="red", bg="white")
        self.feedback_label.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "admin" and password == "password":
            self.feedback_label.config(text="Login successful!", fg="green")
            self.root.after(1000, self.redirect_to_main) 
        else:
            self.feedback_label.config(text="Invalid credentials, try again.", fg="red")

    def redirect_to_main(self):
        self.root.destroy() 
        main_root = Tk()  
        MainPage(main_root)  
        main_root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
