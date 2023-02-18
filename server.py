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

"""
while True:
    rx = client_socket.recv(1024).decode('utf-8')
    print("Client message: ")
    print(rx)
    tx = input("Server message: \n")
    if(tx == "exit"):
        break
    client_socket.send(tx.encode('utf-8'))

#127.0.1.1
#host = socket.gethostbyname(socket.gethostname())
#host = 'localhost'
host = '192.168.0.207'
port = 8080

#Socket for server, IPv4 and TCP
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Adding ip address and port number
server.bind((host,port))

#Listen for one connection
server.listen(1)
print("Awaiting connection...")

while True:
    client, client_server = server.accept()
    print("\n\n\n")
    print("Connection established.")
    message = input("   Input your message: \n")
    if message == "exit":
        print("Server application terminated.")
        break
    client.send(message.encode('utf-8'))
    client.recv(message).decode('utf-8')
    print("             "+message)
               
#Endlessly accept
#Establish client-server connection
client, client_server = server.accept()
#Print when connected
print(f"Connected")
message = client.recv(1024).decode('utf-8')
print(f"Message from client is: {message}")
client.send(f"GO HOME".encode('utf-8'))
client.close()
#print(f"The end")
"""