import socket

class Server:

    clients = []
    nicknames = []
    addresses = []
    threads = []

    def __init__(self,ip,port,ipversion,transport):
        self.ip = ip
        self.port = port
        self.ipversion = ipversion
        self.transport = transport

        if self.ipversion == 4:
            if self.transport == 'TCP':
                server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            elif self.transport == 'UDP':
                pass
            else:
                print('Wrong version of transport protocol, choose between TCP and UDP.')

        elif self.ipversion == 6:
            pass
        else:
            print('Wrong version of IP, choose between 4 and 6.')

        #Add checking to verify whether the IP passed is correct, and port, make
        server_socket.bind((self.ip,self.port))

        print(server_socket)


server = Server('127.0.0.1',55555,4,'TCP')