import socket
import threading
from datetime import datetime

ip = '127.0.0.1'
port = 55555
coding = "utf-8"
buffer = 1024

nickname = input("Enter your nickname: ")

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((ip,port))

stop_condition = threading.Event()

message_recv = ""
message_send = ""

def receive_message():
    while True:

        if stop_condition.is_set():
            break

        global message_send
        global message_recv

        try:
            message_recv = client_socket.recv(buffer).decode(coding)
            if message_recv == 'N1CKN4M3':
                client_socket.send(nickname.encode(coding))
            elif message_recv == 'P4SSW0RD':
                pass
            #    client_socket.send(password.encode(coding))
            elif message_recv == 'T3RM1N4T3':
                client_socket.close()
                stop_condition.set()
                print("Wrong password, connection terminated.")
            elif message_recv == '':
                client_socket.close()
                stop_condition.set()
                if not message_send == '/disconnect':
                    print("Connection terminated by the server side.")
            elif message_recv == '' and not stop_condition.is_set:
                client_socket.close()
                stop_condition.set()
                if not message_send == '/disconnect':
                    print("Connection terminated by the server side.")
            else:
                print(message_recv)

        except:
            client_socket.close()
            stop_condition.set()
            if not message_send == '/disconnect':
                print("Connection terminated by the server side.")

def send_message():
    while True:

        if stop_condition.is_set():
            break

        global message_send
        global message_recv

        if message_recv == 'P4SSW0RD':
            message_send = input("Password")
        else:
            message_send = input("")
        if message_send == "":
            pass
        elif message_send[0] == '/':
            if message_send[1:] == 'disconnect':
                client_socket.send(message_send.encode(coding))
                client_socket.close()
                stop_condition.set()
                print("You are disconnected from the server.")
            elif message_send[1:] == 'admin':
                client_socket.send(message_send.encode(coding))
        else:
            client_socket.send(f'{nickname}: {message_send}'.encode(coding))

receive_thread = threading.Thread(target=receive_message, args=())
receive_thread.start()

send_thread = threading.Thread(target=send_message, args=())
send_thread.start()