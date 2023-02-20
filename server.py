import socket
import threading

#thread for receiving messages
#thread for server command

#Maybe later make it an option to use switch between maybe ipv4/ipv6 and tcp/udp
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Port selection?
port = 8080
server_socket.bind((socket.gethostname(),port))

#What exacly is happening?
server_socket.listen(1)

#List of connected clients and their nicknames, the same values with the same indexes correspond to the same client
addresses = []
nicknames = []

condition = True

def server_command():
    command = input("COMMAND")
    if(command=="end"):
        condition = False
    return condition

while condition:
    client_socket, client_address = server_socket.accept()
    client_socket.send("You succesfully connected to the server. Who are you?".encode("utf-8"))
    print(f"{client_address} connected to the server.")
    addresses.append(client_address)
    client_nickname = client_socket.recv(1024).decode("utf-8")
    print(f"{client_address} nickname is: {client_nickname}")
    nicknames.append(client_nickname)
    #make it a thread
    condition = server_command()
server_socket.close()
print("Server application terminated.")

for i in range(len(nicknames)):
    print(f"The user {nicknames[i]} connected from {addresses[i]}.")

"""
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

s.py file

import socket
import time

HEADERSIZE = 10

#msg = "Welcome to the server!"
#print(f'{len(msg):<{HEADERSIZE}}'+msg)

#AF_INET - ipv4, SOCK_STREAM - tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#gethostbyname() - bassiacly address 127.0.1.1
s.bind((socket.gethostname(),60000))

s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"{address} connected.")
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}'+msg
    clientsocket.send(msg.encode('ascii'))
    #clientsocket.send(bytes("Hello","ascii"))
    while True:
        time.sleep(3)
        msg = f"The rime is!{time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}'+msg
        clientsocket.send(msg.encode('ascii'))
s.close()

print(socket.gethostbyname("me-VirtualBox"))
#print(socket.gethostbyaddr())
#print(socket.gethostbyname_ex())
#print(socket.gethostname())

c.py file

import socket

HEADERSIZE = 10

#AF_INET - ipv4, SOCK_STREAM - tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '192.168.0.25'
#only when there is only one machine
s.connect((ip,60000))

#Buffering is important
while True:
    fullmsg=''
    newmsg=True
    while True:
        msg = s.recv(16)
        if newmsg:
            print(f"New message length: {msg[:HEADERSIZE]}")
            msglen= int(msg[:HEADERSIZE])
            newmsg = False
        fullmsg+=msg.decode("ascii")
        if len(fullmsg)-HEADERSIZE==msglen:
            print("full msg recvd")
            print(fullmsg[HEADERSIZE:])
            newmsg=True
            fullmsg = ''
    print(fullmsg) 

"""