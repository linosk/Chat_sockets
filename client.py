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

def receive_message():
    while True:
        try:
            message = client_socket.recv(buffer).decode(coding)
            if message == 'N1CKN4M3':
                client_socket.send(nickname.encode(coding))
            else:
                print(message)
        #This except does not work
        except:
            print("Connection terminated by the server side.")
            client_socket.close()
            break

def send_message():
    while True:
        message = input("")
        if message == "":
            pass
        else:
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            client_socket.send(f'[{time}]{nickname}: {message}'.encode(coding))

receive_thread = threading.Thread(target=receive_message, args=())
receive_thread.start()

send_thread = threading.Thread(target=send_message, args=())
send_thread.start()

#client_socket.close()