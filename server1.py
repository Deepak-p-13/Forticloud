import socket
import os
import subprocess
import threading
from threading import Thread


def handle_client_connection(conn, addr):
    print(f"[+] Connection established from: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte, "utf-8")
            currentWD = os.getcwd() + "> "
            conn.send(str.encode(output_str + currentWD))
            print(output_str)

    conn.close()

def Terminal():
    s = socket.socket()
    host = "192.168.46.81"
    port = 9999

    s.bind((host, port))
    s.listen(5)
    print(f"[*] Listening as {host}:{port}")

    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client_connection, args=(conn, addr))
        client_thread.start()

def send_file(filename, host, port):
    # Create a TCP socket
       client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
       client_socket.connect((host, port))

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


def receive_file(save_as, port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the address and port
    server_socket.bind(("0.0.0.0", port))
    # Listen for incoming connections
    server_socket.listen(1)

    print(f"Server listening on port {port}...")

    # Accept a client connection
    client_socket, client_address = server_socket.accept()

    try:
        # Open or create a file for writing
        with open(save_as, "wb") as f:
            # Receive data from the client and write it to the file
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)
        print(f"File received and saved as '{save_as}'.")
    finally:
        # Close the client socket
        client_socket.close()
        # Close the server socket
        server_socket.close()




def start_server():
   
    s = socket.socket()
    host = '0.0.0.0'
    port = 8080
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()
    print(f"[*] Listening as {host}:{port}")
    data = conn.recv(1024)
    print(f"Received message from client: {data.decode()}")
    with open('Info.txt', 'r') as file:
        pdw=file.read()
    if  pdw==data.decode():
        conn.sendall(b"correct")
        option = conn.recv(1024)
        option=option.decode()
        save_as = "recent"
        port = 8081
        
        if option=="1":
           Terminal()
        elif option=="2":
           receive_file(save_as, port).start()
          
        elif option=="3":
                file_to_send = input("Enter the file path to send: ")
                server_host =  input("Enter the server IP: ")
                server_port = 8081 
                send_file(file_to_send, server_host, server_port)
    else:
        conn.sendall(b"wrong")

start_server()