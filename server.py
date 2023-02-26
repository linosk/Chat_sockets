import socket
import threading

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
    condition = True

    #TODO - function dedicated for commands from server, add other functions
    def server_commands():
        nonlocal condition
        command = input("")
        if command == "end":
            print("Server forcefully terminated.")
            condition = False
            return

    while condition:
        print("Server started.")
        if len(clients) == 0:
            print("Awaiting for connections...")
        t1 = threading.Thread(target=server_commands, args=())
        t1.start()
        #server_commands()
        client_socket, client_address = server_socket.accept()
        client_nickname = client_socket.recv(buffer).decode(coding)
        print(client_nickname)
        t1.join()

start()