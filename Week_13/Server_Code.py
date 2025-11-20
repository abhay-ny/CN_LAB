import socket
import os

HOST = '127.0.0.1'     # Localhost
PORT = 5000            # Port to listen on

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server started. Listening on {HOST}:{PORT}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        filename = conn.recv(1024).decode()

        # Check if file exists
        if os.path.isfile(filename):
            conn.sendall("FOUND".encode())

            with open(filename, 'r') as f:
                data = f.read()

            conn.sendall(data.encode())
        else:
            conn.sendall("NOT_FOUND".encode())

        conn.close()

if __name__ == "__main__":
    start_server()
