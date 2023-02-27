import socket
import threading
import sys
import signal

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
        #condition_two = True
        while True:
            command = input("")
            if command == "end":
                print("Server forcefully terminated.")
                #for client in clients:
                #    client.send("S3rv3r f0rc3f8ll7 t3rm1n4ted.".encode(coding))
                #    client.close()
                #server_socket.close()
                #condition_two = False
                #condition = False
                condition = False
                break
                #sys.exit(1)
            elif command == "users":
                if len(nicknames) == 0:
                    print("Currently there are no users connected.")
                else:
                    print(nicknames)

    def get_user_input():
        return input("")

    print("Server started.")
    print("Awaiting for connections...")

    while condition:
            t1 = threading.Thread(target=get_user_input, args=())
            t1.start()
            client_socket, client_address = server_socket.accept()
            #print(f"{client_socket} tries to connect to the server.")
            #client_socket.send("N1ckn4m3".encode(coding))
            #client_nickname = client_socket.recv(buffer).decode(coding)
#   
            #clients.append(client_socket)
            #addresses.append(client_address)
            #nicknames.append(client_nickname)
#   
            #send_to_all_clients(f'{client_nickname} just connected to the server.'.encode(coding))

            t1.join()
            t2.join()

start()