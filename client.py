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

def receive_message():
    while True:

        if stop_condition.is_set():
            break

        try:
            message = client_socket.recv(buffer).decode(coding)
            if message == 'N1CKN4M3':
                client_socket.send(nickname.encode(coding))
            elif message == '':
                client_socket.close()
                stop_condition.set()
                print("Connection terminated by the server side.")
            elif message == '' and not stop_condition.is_set:
                client_socket.close()
                stop_condition.set()
                print("Connection terminated by the server side.")
            else:
                print(message)
        #This except does not work
        except:
            print("Connection terminated by the server side.")
            client_socket.close()
            stop_condition.set()

def send_message():
    while True:

        if stop_condition.is_set():
            break

        message = input("")
        if message == "":
            pass
        elif message[0] == '/':
            if message[1:] == 'disconnect':
                client_socket.send(message.encode(coding))
                client_socket.close()
                stop_condition.set()
                print("You are disconnected from the server.")
        else:
            #Time of message should be added at the server side
           #now = datetime.now()
           #time = now.strftime("%H:%M:%S")
            #client_socket.send(f'[{time}]{nickname}: {message}'.encode(coding))
            client_socket.send(f'{nickname}: {message}'.encode(coding))

receive_thread = threading.Thread(target=receive_message, args=())
receive_thread.start()

send_thread = threading.Thread(target=send_message, args=())
send_thread.start()

#Check whether threads are running
if stop_condition.is_set():
    print(receive_thread.is_alive())
    print(send_thread.is_alive())

#client_socket.close()