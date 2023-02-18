import sys
import threading

"""
while True:
    rx = client_socket.recv(1024).decode('utf-8')
    print("Client message: ")
    print(rx)
    tx = input("Server message: \n")
    if(tx == "exit"):
        break
    client_socket.send(tx.encode('utf-8'))
"""

def send_message(socket,encoding):
    tx = input("Your message: \n")
    if(tx=="exit"):
        sys.exit("Connection terminated.")
    socket.send(tx.encode(encoding))

def recv_message(socket,encoding,size):
    rx = socket.recv(size).decode(encoding)
    print("Their message: ")
    print(rx)

def comm_server(socket,encoding,size):
    #while True:
        t1 = threading.Thread(target=recv_message, args=[socket,encoding,size])
        t2 = threading.Thread(target=send_message, args=[socket,encoding])
        t1.start()
        t2.start()

def comm_client(socket,encoding,size):
    #while True:
        t1 = threading.Thread(target=send_message, args=[socket,encoding])
        t2 = threading.Thread(target=recv_message, args=[socket,encoding,size])
        t1.start()
        t2.start()