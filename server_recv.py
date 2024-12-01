import socket
def receive_file():
        while True:
            # Create a TCP socket
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Bind the socket to the address and port
            server_socket.bind(("192.168.101.81", 5555))
            # Listen for incoming connections
            server_socket.listen(1)
            print("Server listening on port 5555...")
            # Accept a client connection
            client_socket, client_address = server_socket.accept()
            # Accept a client connection
            save_as=client_socket.recv(1024)
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

receive_file()