import socket
import threading
from datetime import datetime

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

#Sever broadcasts message to every client
def broadcast_message(message, type_of_broadcast):
    message_decoded = message.decode(coding)
    print(f'Message will be sent to {nicknames}.')
    if type_of_broadcast == 'client_message':
        for client in clients:
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            client.send(f'[{time}]{message_decoded}'.encode(coding))
    elif type_of_broadcast == 'connection_info':
        for client in clients:
            client.send(message)
    else:
        pass

def remove_connection_records(index):
    clients.remove(clients[index])
    nicknames.remove(nicknames[index])
    addresses.remove(addresses[index])
    threads.remove(threads[index])

def handle_client(client):
    stop_condition = threading.Event()
    index = clients.index(client)
    nickname = nicknames[index]
    while True:

        if stop_condition.is_set():
            print(f'{nickname} disconnected from the server.')
            broadcast_message(f'{nickname} disconnected from the server.'.encode(coding),'connection_info')
            break

        try:
            message = client.recv(buffer)
            message_decoded = message.decode(coding)
            if message_decoded[0] == '/':
                if message_decoded[1:] == 'disconnect':
                    if client in clients:
                        #Client willingly disconnected
                        print('A')
                        stop_condition.set()
                        client.close()
                        remove_connection_records(index)

            else:
                broadcast_message(message,'client_message')
        except:
            
            #Disconnect from the client side possibly unwillingly
            if client in clients:
                print('B')
                stop_condition.set()
                client.close()
                remove_connection_records(index)

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

            broadcast_message(f'{client_nickname} joined the chat.'.encode(coding),'connection_info')
            client_socket.send('You are connected to the server.'.encode("utf-8"))

            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
            if client_thread not in threads:
                threads.append(client_thread)

        except KeyboardInterrupt:
            server_socket.close()
            break

print("Awaiting connections...")

server_run()