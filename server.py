import socket

#host = socket.gethostname() 
host = '127.0.0.1'
#TODO - allow to choose port
port = 55555

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#TODO - allow given user to reconnect
server_socket.bind((host,port))

#TODO - (maybe) pass value in listen
server_socket.listen()

print("Awaiting for connection...")
server_socket.accept()

print("User connected.")