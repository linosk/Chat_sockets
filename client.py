import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#TODO make user choose port number and IP address
host = '127.0.0.1'
port = 55555

client_socket.connect((host,port))

print("Connection established.")