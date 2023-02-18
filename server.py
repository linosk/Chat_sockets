import socket
import functions

#Ip address of current computer and selected port
host_address = '192.168.0.207'
port = 8080

#Socket for server(IPv4 and TCP)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Binding socket
server_socket.bind((host_address,port))

#Listen for 1 connection
server_socket.listen(1)

#Accept connection
client_socket, client_address = server_socket.accept()

print("Connection established")
client_socket.send("Connection established".encode('utf-8'))
print("\n")

functions.comm_server(client_socket,'utf-8',1024)

#Watch and create https://www.youtube.com/watch?v=Lbfe3-v7yE0&list=PLQVvvaa0QuDdzLB_0JSTTcl8E8jsJLhR5&ab_channel=sentdex
