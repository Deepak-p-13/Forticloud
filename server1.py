import socket
import os
import subprocess
import threading
from threading import Thread

while True:
    def handle_client_connection(conn, addr):
        print(f"[+] Connection established from: {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                break

            if data[:2].decode("utf-8") == 'cd':
                os.chdir(data[3:].decode("utf-8"))

            if len(data) > 0:
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
                output_byte = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_byte, "utf-8")
                currentWD = os.getcwd() + "> "
                conn.send(str.encode(output_str + currentWD))
                print(output_str)

        conn.close()


    def Terminal():
        s = socket.socket()
        host = "192.168.101.81"
        port = 9999

        s.bind((host, port))
        s.listen(5)
        print(f"[*] Listening as {host}:{port}")

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client_connection, args=(conn, addr))
            client_thread.start()


    def start_server():
        s = socket.socket()
        host = '192.168.101.81'
        port = 8080
        s.bind((host, port))
        s.listen(5)
        conn, addr = s.accept()
        print(f"[*] Listening as {host}:{port}")
        data = conn.recv(1024)
        print(f"Received message from client: {data.decode()}")
        with open('Info.txt','r') as file:
            pdw = file.read()
        if pdw == data.decode():
            conn.sendall(b"correct")
            option = conn.recv(1024)
            option = option.decode()
            save_as = "recent"
            port = 8081

            if option == "1":
                Terminal()
            elif option == "2":
                receive_file(save_as, port).start()

            elif option == "3":
                server_host = "192.168.101.81"
                server_port = 8081
                send_file(server_host, server_port)
        else:
            conn.sendall(b"wrong")


    start_server()
