import socket

host = '192.168.186.1'
port = 9090
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send("Hello!".encode('utf-8'))
print(client.recv(1024))
