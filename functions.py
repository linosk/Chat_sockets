import os
import signal
import sys
import threading

def send_message(socket,encoding):
    while True:
        tx = input()
        if(tx=="exit"):
            #socket.close()
            socket.shutdown("SHUT_RDWR")
            #sys.exit("Connection terminated.")
            os.kill(os.getpid(), signal.SIGKILL)
        #try:
        #    socket.send(tx.encode(encoding))
        #    print("Your message: "+tx)
        #except:
        #    print("Connection lost.\n")
        #    socket.close()
        #    sys.exit("Application terminated.")

def recv_message(socket,encoding,size):
    while True:
        #try:
            rx = socket.recv(size).decode(encoding)
            print("Their message: "+rx)
        #except:
        #    print("Connection lost.\n")
        #    socket.close()
        #    sys.exit("Application terminated.")

def comm_server(socket,encoding,size):
    t1 = threading.Thread(target=recv_message, args=[socket,encoding,size])
    t2 = threading.Thread(target=send_message, args=[socket,encoding])
    t1.start()
    t2.start()

def comm_client(socket,encoding,size):
    t1 = threading.Thread(target=send_message, args=[socket,encoding])
    t2 = threading.Thread(target=recv_message, args=[socket,encoding,size])
    t1.start()
    t2.start()