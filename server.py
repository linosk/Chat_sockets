import socket
import threading
import sys

#host = socket.gethostname() 
host = '127.0.0.1'
#TODO - allow to choose port
port = 55555
#TODO - allow a server to change encoding - MAYBE
coding = "utf-8"
#TODO - take care of cases when the buffer is overflown, maybe use header
buffer = 1024

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#TODO - allow given user to reconnect
server_socket.bind((host,port))

#TODO - (maybe) pass value in listen
server_socket.listen()

def start():
    clients = []
    addresses = []
    nicknames = []
    condition = True

    def send_to_all_clients(message):
        for client in clients:
            client.send(message)

    #TODO - function dedicated for commands from server, add other functions
    def server_commands():
        nonlocal condition
        while condition:
            print("SA")
            command = input("")
            if command == "end":
                print("Server forcefully terminated.")
                #for client in clients:
                #    client.send("S3rv3r f0rc3f8ll7 t3rm1n4ted.".encode(coding))
                #    client.close()
                server_socket.close()
                condition = False
                return
            elif command == "users":
                if len(nicknames) == 0:
                    print("Currently there are no users connected.")
                else:
                    print(nicknames)

    print("Server started.")
    print("Awaiting for connections...")

    while condition:
        print(condition)
        t1 = threading.Thread(target=server_commands, args=())
        t1.start()
        client_socket, client_address = server_socket.accept()
        print(f"{client_socket} tries to connect to the server.")
        client_socket.send("N1ckn4m3".encode(coding))
        client_nickname = client_socket.recv(buffer).decode(coding)

        clients.append(client_socket)
        addresses.append(client_address)
        nicknames.append(client_nickname)

        send_to_all_clients(f'{client_nickname} just connected to the server.'.encode(coding))

        #server_commands()

        #t1.join()

start()