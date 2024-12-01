import tkinter as tk
from tkinter import messagebox
import customtkinter
from client import start

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def sign_up():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Validate input (basic validation)
    if not (name and phone and email and password):
        messagebox.showerror("Error", "All fields are required")
        return

    # Here, you can proceed with the sign-up functionality, such as saving the data to a database or file.
    # For demonstration purposes, let's just print the entered details.
    print("Name:", name)
    print("Phone Number:", phone)
    print("Email Address:", email)
    print("Password:", password)
    # You can then add the code to actually sign up the user, such as calling a function from the 'start' module.

# Define the sign-up window
def sign_up_window():
    root_signup = customtkinter.CTk()
    root_signup.geometry(f"{500}x{500}")
    root_signup.title("SIGN UP")

    frame = customtkinter.CTkFrame(master=root_signup, width=450, height=450, corner_radius=10)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    label_title = customtkinter.CTkLabel(master=frame, width=400, height=40, corner_radius=10,
                                         fg_color=("gray70", "gray35"), text="Sign Up Here!")
    label_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    name_label = customtkinter.CTkLabel(master=frame, width=150, height=30, corner_radius=10, text="Name:")
    name_label.place(relx=0.3, rely=0.3, anchor=tk.CENTER)
    name_entry = customtkinter.CTkEntry(master=frame, corner_radius=20, width=200)
    name_entry.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

    phone_label = customtkinter.CTkLabel(master=frame, width=150, height=30, corner_radius=10, text="Phone Number:")
    phone_label.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
    phone_entry = customtkinter.CTkEntry(master=frame, corner_radius=20, width=200)
    phone_entry.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

    email_label = customtkinter.CTkLabel(master=frame, width=150, height=30, corner_radius=10, text="Email Address:")
    email_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
    email_entry = customtkinter.CTkEntry(master=frame, corner_radius=20, width=200)
    email_entry.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

    password_label = customtkinter.CTkLabel(master=frame, width=150, height=30, corner_radius=10, text="Password:")
    password_label.place(relx=0.3, rely=0.6, anchor=tk.CENTER)
    password_entry = customtkinter.CTkEntry(master=frame, corner_radius=20, width=200, show="*")
    password_entry.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

    sign_up_button = customtkinter.CTkButton(master=frame, text="SIGN UP", corner_radius=3, command=sign_up, width=400)
    sign_up_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    root_signup.mainloop()

sign_up_window()
