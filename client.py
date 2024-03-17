import socket
import sys
import hashlib
import os



class start:
    def signup():
        print("sign")
        name=input("Name: ")
        pone=input("ph.no: ")#check for int
        psd=input("password: ")
        all=name+" "+pone+" "+psd
        hashed_password = hashlib.sha256(all.encode()).hexdigest()
        host = '192.168.46.81'
        port = 1234

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        client_socket.sendall(hashed_password.encode())

        client_socket.close()

    def create_socket():
        try:
            global host
            global port
            global s
            host = "192.168.46.81"  # Change this to the IP address of the server
            port = 9999
            s = socket.socket()

        except socket.error as msg:
            print("Socket creation error: " + str(msg))

    def connect_to_server():
        try:
            global host
            global port
            global s
            s.connect((host, port))

        except socket.error as msg:
            print("Connection to server failed: " + str(msg))
            sys.exit()

    def send_commands():
        try:
            while True:
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
    def receive_file(save_as,client_socket):
        try:
            client_socket.sendall(save_as.encode())
            # Open or create a file for writing
            with open("recived.txt", "wb") as f:
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
 
        
        

def main():
    print("1.Signup")
    print("2.login")
    a=int(input("Choose the option"))
    if a==1:
        start.signup()

    elif a==2: 
        print("login")
        name=input("Name: ")
        pone=input("ph.no: ")         #check for int
        psd=input("password: ")
        all=name+" "+pone+" "+psd
        hashed_password = hashlib.sha256(all.encode()).hexdigest()
        host = '192.168.46.81'
        port = 8080

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        client_socket.sendall(hashed_password.encode())
        ans=client_socket.recv(1024)
        ans=ans.decode()
        if ans=="correct":
            print("correct\n choose the option:\n 1]Terminal\n 2]upload files\n 3]dowload files")
            select=int(input("Eneter the option:"))
            client_socket.sendall(str(select).encode())
            if select==1:
                start.create_socket()
                start.connect_to_server()
                start.send_commands()
            elif select==2:
                file_to_send = input("Enter the file path to send: ")
                server_host =  input("Enter the server IP: ")
                server_port = 8081
                start.send_file(file_to_send, server_host, server_port)
            elif select==3:
                 save_as = input("Enter the filename to recive: ")
                 start.receive_file(save_as,client_socket)
               

    
        
      
main()