import socket
import functions

#Ip address of target computer and selected port
host_address = '192.168.0.207'
port = 8080

#Socket for communication
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect to server
client_socket.connect((host_address,port))

#while True:
rx = client_socket.recv(1024).decode('utf-8')
#message = client_socket.recv(1024).decode('utf-8')
print(rx+"\n")

functions.comm_client(client_socket,'utf-8',1024)