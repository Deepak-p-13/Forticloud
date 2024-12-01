import tkinter as tk
import subprocess
import customtkinter
from client import start
import threading

def dashboard_1():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    def uploadbutt():
        button_upload_pressed.set(True)
        login_input()
    
    def downloadbutt():
        button_download_pressed.set(True)
        login_input()
    
    def login_input(event=None):
        # Retrieve the input from the entry field
        command = input_entry2.get()
        input_entry2.delete(0, tk.END)  # Clear the entry field
        h = command
        if button_upload_pressed.get():  # Check if Upload button is pressed
            start.send_file(h,"10.0.10.79",5555)  # Call the send_file function with the entry text
        elif button_download_pressed.get():  # Check if Download button is pressed
            start.receive_file(h,"10.0.10.79",5550)  # Call the receive_file function with the entry text

    def sign():
        start.signup(name=entry_1.get(), psd=entry_2.get())

    def show_cmd_output(event=None):
        # Get command from entry widget
        command = input_entry.get()
        input_entry.delete(0, tk.END)

        # Display entered command
        output_text.insert(tk.END, f"> {command}\n", "command")
        output_text.see(tk.END)

        # Send command to cmd process
        cmd_process.stdin.write(command + '\n')
        cmd_process.stdin.flush()

    def update_output():
        while True:
            # Read cmd output
            output = cmd_process.stdout.readline()

            if output == '' and cmd_process.poll() is not None:
                break

            # Display cmd output
            output_text.insert(tk.END, output)
            output_text.see(tk.END)

    # Define the login page window
    root_login = customtkinter.CTk()
    root_login.geometry(f"{700}x500")
    root_login.title("LOGIN PAGE")

    # Add some widgets for login page
    frame = customtkinter.CTkFrame(master=root_login, width=450, height=450, corner_radius=10)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    label_1 = customtkinter.CTkLabel(master=frame, width=400, height=60, corner_radius=10,
                                     fg_color=("gray70", "gray35"), text="Dashboard")
    label_1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    button_download_pressed = tk.BooleanVar()
    button_upload_pressed = tk.BooleanVar()

    button_download = customtkinter.CTkButton(master=frame, text="DOWNLOAD", corner_radius=3, width=180,
                                              command=downloadbutt)
    button_download.place(relx=0.18, rely=0.43, anchor=tk.N)

    input_entry2 = tk.Entry(master=frame)
    input_entry2.place(relx=0.17, rely=0.5, anchor=tk.N)
    

    button_upload = customtkinter.CTkButton(master=frame, text="UPLOAD", corner_radius=3,command=uploadbutt, width=180)
    button_upload.place(relx=0.18, rely=0.55, anchor=tk.N)

    # Entry widget for user input
    input_entry = tk.Entry(master=frame)
    input_entry.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    input_entry.bind("<Return>", show_cmd_output)

    # Text widget to display cmd output
    output_text = tk.Text(master=frame, height=15, width=35)
    output_text.place(relx=0.68, rely=0.5, anchor=tk.CENTER)

    # Start the command prompt subprocess
    cmd_process = subprocess.Popen(["cmd.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, universal_newlines=True)

    # Start a thread to continuously update output
    output_thread = threading.Thread(target=update_output)
    output_thread.daemon = True
    output_thread.start()

    root_login.mainloop()

if __name__ == "__main__":
    dashboard_1()
