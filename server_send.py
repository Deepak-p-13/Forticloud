import socket
import os


def send_file():
    try:
        # Create a TCP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the address and port
        server_socket.bind(("192.168.101.81", 5550))
        # Listen for incoming connections
        server_socket.listen(1)
        print(f"Server listening on port {5550}...")
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        file_name = client_socket.recv(1024).decode()

        try:
            if os.path.exists(file_name):  # Check if the file exists
                file_size = os.path.getsize(file_name)
            
                print(file_size)
                client_socket.send(str(file_size).encode())  # Send file size as a string
                # Open the file to be sent in binary mode
                with open(file_name, "rb") as file:
                    # Send file data in chunks
                    while True:
                        data = file.read(1024)
                        if not data:
                            break
                        client_socket.sendall(data)
                client_socket.send(b"<END>")
                print("File sent successfully.")
            else:
                client_socket.send(b"File not found")
        except Exception as e:
            print(f"Error sending file: {e}")
        finally:
            client_socket.close()
    except Exception as e:
        print(f"Error establishing server connection: {e}")
while  True:
 send_file()