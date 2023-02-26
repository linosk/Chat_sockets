import socket
import sys
import threading

#TODO make user choose port number, IP address, and maybe coding
host = '127.0.0.1'
port = 55555
coding = "utf-8"
#TODO - take care of cases when the buffer is overflown, maybe use header
buffer = 1024

nickname = input("Enter your nickname: ")

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    client_socket.connect((host,port))
except:
    print("Unable to connect.")
    sys.exit(0)

def receive_message():
    while True:
        recv_message = client_socket.recv(buffer).decode(coding)
        if recv_message == "N1ckn4m3":
            client_socket.send(nickname.encode(coding))
        elif recv_message == "S3rv3r f0rc3f8ll7 t3rm1n4ted":
            print("Server forcefully terminated.")
            client_socket.close()
            break
        else:
            print(recv_message)

def send_message():
    pass
#client_socket.send(nickname.encode(coding))

t1 = threading.Thread(target=receive_message,args=())
t1.start()

print("Connection established.")