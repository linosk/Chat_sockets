import socket

#TODO make user choose port number, IP address, and maybe coding
host = '127.0.0.1'
port = 55555
coding = "utf-8"
#TODO - take care of cases when the buffer is overflown, maybe use header
buffer = 1024

nickname = input("Enter your nickname: ")

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

client_socket.send(nickname.encode(coding))

print("Connection established.")