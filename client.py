import socket
import sys
import hashlib
import tkinter as tk
from tkinter import ttk
import threading
import time

class start:
    @staticmethod
    def signup(name, psd):
        print("sign")
        pone = "123"  # check for int
        print(name,psd)
        all = name + " " + pone + " " + psd
        hashed_password = hashlib.sha256(all.encode()).hexdigest()
        host = '25.45.108.51'
        port = 1234
        print(hashed_password)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        client_socket.sendall(hashed_password.encode())

        client_socket.close()

    @staticmethod
    def create_socket():
        try:
            host = "25.45.108.51"  # Change this to the IP address of the server
            port = 9999
            s = socket.socket()
            return s
        except socket.error as msg:
            print("Socket creation error: " + str(msg))

    @staticmethod
    def connect_to_server(s):
        try:
            host = "25.45.108.51"  # Change this to the IP address of the server
            port = 9999
            s.connect((host, port))
            print("continue")
        except socket.error as msg:
            print("Connection to server failed: " + str(msg))
            sys.exit()

    @staticmethod
    def send_commands(s):
        try:
            while True:
                print("Enter command123")
                cmd = input("Enter command: ")  # Prompt the user for input
                if cmd == 'quit':
                    s.close()
                    sys.exit()

                if len(str.encode(cmd)) > 0:
                    s.send(str.encode(cmd))
                    server_response = str(s.recv(1024), "utf-8")
                    print(server_response, end="")
        except EOFError:
            print("Error: Interactive input is not supported in this environment.")
            sys.exit()

    @staticmethod
    def send_file(filename, host, port):
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        client_socket.connect((host, port))
        client_socket.sendall(filename.encode())
        try:
            # Open the file to be sent
            with open(filename, "rb") as f:
                # Read the file in chunks and send it
                while True:
                    chunk = f.read(1024)
                    if not chunk:
                        break
                    client_socket.sendall(chunk)
            print("File sent successfully.")
        finally:
            # Close the socket
            client_socket.close()

    @staticmethod   
    
    
    def receive_file(file_name, host, port):
        def receive_thread():
            nonlocal received_size

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))

            try:
                client_socket.send(file_name.encode())
                file_size_str = client_socket.recv(1024).decode()
                file_size = int(file_size_str)
                file = open(file_name, "wb")

                start_time = time.time()  # Record start time for speed calculation
                last_update_time = start_time
                last_received_size = 0

                while received_size < file_size:
                    data = client_socket.recv(1024)
                    received_size += len(data)
                    file.write(data)

                    # Update progress bar
                    progress_window.after(10, update_progress, received_size, file_size)

                    # Update speed and transferred values every second
                    current_time = time.time()
                    if current_time - last_update_time >= 1:
                        elapsed_time = current_time - start_time
                        speed = (received_size - last_received_size) / 1024 / 1024 / (current_time - last_update_time)  # MB/s
                        speed_label.config(text=f"Speed: {speed:.2f} MB/s")
                        transfer_label.config(text=f"Transferred: {received_size / 1024 / 1024:.2f} MB")
                        last_update_time = current_time
                        last_received_size = received_size

                file.close()
                end_time = time.time()  # Record end time for speed calculation
                elapsed_time = end_time - start_time
                speed = (received_size / 1024 / 1024) / elapsed_time  # Calculate speed in MB/s
                speed_label.config(text=f"Speed: {speed:.2f} MB/s")
                transfer_label.config(text=f"Transferred: {received_size / 1024 / 1024:.2f} MB")

                print(f"File received and saved as '{file_name}'.")
                progress_window.destroy()
            finally:
                client_socket.close()

        def update_progress(received, total):
            progress_bar['value'] = received / total * 100

        received_size = 0

        progress_window = tk.Toplevel()
        progress_window.title("File Transfer Progress")

        progress_bar = ttk.Progressbar(progress_window, length=300, mode='determinate')
        progress_bar.pack(padx=10, pady=10)

        speed_label = tk.Label(progress_window, text="Speed: 0 MB/s")
        speed_label.pack()
        
        transfer_label = tk.Label(progress_window, text="Transferred: 0 MB")
        transfer_label.pack()

        # Start a new thread for the file transfer
        thread = threading.Thread(target=receive_thread)
        thread.start()
# Example usage:
# receive_file_with_progress()


    

    @staticmethod
    def cmd():
       s = start.create_socket()
       start.connect_to_server(s)
       start.send_commands(s)

    @staticmethod
    def upload():
       file_to_send = input("Enter the file path to send: ")
       server_host = "25.45.108.51"
       server_port = 8081
       start.send_file(file_to_send, server_host, server_port)

    @staticmethod
    def main(name, psd):
        print("1.Signup")
        print("2.login")
        print("login")
        pone = "123"  # check for int
        all = name + " " + pone + " " + psd
        hashed_password = hashlib.sha256(all.encode()).hexdigest()
        host = '25.45.108.51'
        port = 8080

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(hashed_password.encode())
        ans = client_socket.recv(1024)
        ans = ans.decode()
        if ans == "correct":
            from dashboard import dashboard_1
            # print("correct\n choose the option:\n 1]Terminal\n 2]upload files\n 3]dowload files")
            # print("\nEnter the option:")
            # select = int(input(""))
            client_socket.sendall(str("1").encode())
            dashboard_1()


# if __name__ == "__main__":
#     start.main("username", "password")  # Pass your username and password here
#     start.signup("username", "password")
#     start.upload()
#     start.cmd()


