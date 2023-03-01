import socket
import threading
import time

ip = '127.0.0.1'
port = 55555
coding = "utf-8"
buffer = 1024

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((ip,port))
server_socket.listen()

#Sockets
clients = []
#Nicknames
nicknames = []
#Addresses
addresses = []
#Threads
threads = []

stop_condition = threading.Event()

#Sever broadcasts message to every client
def broadcast_message(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:

        if stop_condition.is_set():
            break

        try:
            message = client.recv(buffer)
            message_decoded = message.decode(coding)
            if message_decoded[0] == '/':
                if message_decoded[1:] == 'disconnect':
                    client.close()
                    #time.sleep(0.5)
                    index = clients.index(client)
                    clients.remove(index)
                    #nickname = nicknames[index]
                    nicknames.remove(index)
                    addresses.remove(index)
                    threads.remove(index)
                    #broadcast_message(f'{nickname} disconnected from the server.')
                    stop_condition.set()

            else:
                broadcast_message(message)
        except:
            pass
            #client.send('Connection terminated.')
            #client.close()
            #break

def server_run():
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            client_socket.send('N1CKN4M3'.encode(coding))
            client_nickname = client_socket.recv(buffer).decode(coding)
            print(f'{client_socket} tries to connect from {client_address} and is called {client_nickname}')

            clients.append(client_socket)
            nicknames.append(client_nickname)
            addresses.append(client_address)

            broadcast_message(f'{client_nickname} joined the chat.'.encode(coding))
            client_socket.send('You are connected to the server.'.encode("utf-8"))

            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
            if client_thread not in threads:
                threads.append(client_thread)

        except KeyboardInterrupt:
            #server_socket.close()
            break

server_run()