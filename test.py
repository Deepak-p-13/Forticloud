import tkinter as tk
import subprocess
import customtkinter

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def update_output():
    # Read cmd output
    output = cmd_process.stdout.readline()
    print("Output:", output)

    # Display cmd output
    if output:
        output_text.insert(tk.END, output)
        output_text.see(tk.END)
    root.after(100, update_output)  # Check for new output after 100 milliseconds


def start_cmd_process():
    global cmd_process
    cmd_process = subprocess.Popen(["cmd.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, universal_newlines=True)
    print("CMD process started")
    update_output()


root = tk.Tk()
root.geometry(f"{800}x600")
root.title("Command Prompt in Python Frame")

frame = customtkinter.CTkFrame(master=root, width=700, height=500, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

output_text = tk.Text(master=frame, wrap=tk.WORD)
output_text.pack(fill=tk.BOTH, expand=True)

start_button = customtkinter.CTkButton(master=frame, text="Start Command Prompt", corner_radius=3,
                                       command=start_cmd_process, width=180)
start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

root.mainloop()
