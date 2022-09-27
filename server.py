
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

while True:
    
    message, address = server_socket.recvfrom(1024)
    command = ""
    if message == b"11":
        command = "forward"
    print(f"Received {command}")
    server_socket.sendto(message, address)
    