import socket

def start_server(host, port):
    host = "192.168.101.81"  # Set your server IP address
    port = 1234 
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind to the address and port
    s.bind((host, port))
    # Listen for incoming connections
    s.listen(5)  # Backlog of 5

    print(f"Server listening on {host}:{port}...")

    while True:
        # Accept a connection
        conn, addr = s.accept()
        print(f"Connected to {addr}")

        # Handle the connection in a separate function
        handle_connection(conn)

def handle_connection(conn):
    with conn:
        

        # Receive the file from the client
        with open('helloclient.txt', 'wb') as f:
            print('File opened')
            while True:
                print('Receiving data...')
                try:
                    data = conn.recv(1024)
                except ConnectionResetError:
                    print("Connection closed by client.")
                    break
                if not data:
                    print("End of transmission.")
                    break
                print('Data received: %s' % data)
                f.write(data)

        print('File received successfully')
        conn.close()
        print('Connection closed')

if __name__ == "__main__":
    start_server(0,0)
