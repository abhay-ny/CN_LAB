import socket
import os

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
BUFFER_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print(f"UDP Server is running on {SERVER_IP}:{SERVER_PORT}")

while True:
    filename, client_addr = sock.recvfrom(BUFFER_SIZE)
    filename = filename.decode().strip()
    print(f"Client requested file: {filename}")

    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = f.read()
        sock.sendto(data.encode(), client_addr)
    else:
        sock.sendto("File not found".encode(), client_addr)
