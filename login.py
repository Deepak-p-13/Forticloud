import tkinter
import threading
import customtkinter
from client import start

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def login_window():
    def login_input():
        username = entry_1.get()
        password = entry_2.get()
        threading.Thread(target=start.main, args=(username, password)).start()

    def sign():
        username = entry_1.get()
        password = entry_2.get()
        threading.Thread(target=start.signup, args=(username, password)).start()

    # Define the login page window
    root_login = customtkinter.CTk()
    root_login.geometry(f"{500}x{500}")
    root_login.title("LOGIN PAGE")

    # Add some widgets for login page
    frame = customtkinter.CTkFrame(master=root_login, width=450, height=450, corner_radius=10)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label_1 = customtkinter.CTkLabel(master=frame, width=400, height=60, corner_radius=10,
                                      fg_color=("gray70", "gray35"), text="Please Login! \nHint: Username=ABC, Pass=123")
    label_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    entry_1 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Username")
    entry_1.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

    entry_2 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, show="*", placeholder_text="Password")
    entry_2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    button_login = customtkinter.CTkButton(master=frame, text="Login", corner_radius=3, command=login_input, width=400)
    button_login.place(relx=0.5, rely=0.7, anchor=tkinter.N)

    button_sign = customtkinter.CTkButton(master=frame, text="Sign in", corner_radius=3, command=sign, width=400)
    button_sign.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    root_login.mainloop()

login_window()