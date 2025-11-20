import socket

HOST = '127.0.0.1'   # Server IP
PORT = 5000          # Server Port

def request_file():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    filename = input("Enter the filename to request: ").strip()
    client_socket.sendall(filename.encode())

    status = client_socket.recv(1024).decode()

    if status == "FOUND":
        print("\n--- File Contents Received ---\n")
        data = client_socket.recv(4096).decode()
        print(data)
    else:
        print("File not found on the server.")

    client_socket.close()

if __name__ == "__main__":
    request_file()
