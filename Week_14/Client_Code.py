import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
BUFFER_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter file name to request: ")

sock.sendto(filename.encode(), (SERVER_IP, SERVER_PORT))

data, addr = sock.recvfrom(BUFFER_SIZE)
print("\n----- Server Response -----")
print(data.decode())
