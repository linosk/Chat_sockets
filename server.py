import socket
import threading
from datetime import datetime

class Server:

    #There may be some redundancy in checking whether the ipv4 address is correct
    def __check_ipv4__(self,ip_address):

        if len(ip_address)<7 or len(ip_address)>15:
            print(f'{ip_address} is not correct ipv4 address.')
            return -1
        
        if ip_address.count('.') != 3:
            print(f'{ip_address} is not correct ipv4 address.')
            return -1
        
        buffer = ip_address
        index = buffer.find('.')
        try:
            first_field = int(buffer[:index])
        except:
            print(f'{ip_address} is not correct ipv4 address.')
            return -1

        buffer = buffer[index+1:]
        index = buffer.find('.')
        try:
            second_field = int(buffer[:index])
        except:
            print(f'{ip_address} is not correct ipv4 address.')
            return -1

        buffer = buffer[index+1:]
        index = buffer.find('.')
        try:
            third_field = int(buffer[:index])
        except:
            print(f'{ip_address} is not correct ipv4 address.')
            return -1

        try:
            fourth_field = int(buffer[index+1:])
        except:
            print(f'{ip_address} is not correct ipv4 address.')
            return -1
        
        if (first_field<0 or first_field>255) or (second_field<0 or second_field>255) or (third_field<0 or third_field>255) or (fourth_field<0 or fourth_field>255):
            print(f'{ip_address} is not correct ipv4 address.')
            return -1
    
    #At the moment well-known and registered port numbers are not usable
    def __check_port_number__(self,port_number):

        if port_number < 0 or port_number > 65535:
            print(f'{port_number} is not correct port number.')
            return -1

        if port_number < 1024:
            print(f'{port_number} is a well-known port number, select a port number from range 49152-65535.')
            return -1
        
        if port_number < 49152:
            print(f'{port_number} is a registered port number, select a port number from range 49152-65535.')
            return -1

    #At the momment only ipv4 addresses can be used in combination with TCP protocol
    def __init__(self,ip_version,transport_protocol,ip_address,port_number):

        if ip_version == 4:
            self.ip_version = 4
        elif ip_version == 6:
            return
        else:
            print('Wrong ip version.')
            return

        if transport_protocol == 'TCP':
            self.transport_protocol = 'TCP'
        elif transport_protocol == 'UDP':
            return
        else:
            print('Wrong transport protocol.')
            return

        if self.ip_version == 4:
            if self.__check_ipv4__(ip_address) == -1 or self.__check_port_number__(port_number) == -1:
                return
            else:
                self.ip_address = ip_address
                self.port_number = port_number

        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.clients = []
        self.nicknames = []
        self.addresses = []
        self.threads = []

        self.coding = 'utf-8'
        self.buffer = 1024 #Need to think about the case very sent message is over the buffer size

        self.server_socket.bind((self.ip_address,self.port_number))

    def __broadcast_message__(self,message,type):
            #Type should be either msg or info
            #Msg messages are messages sent by clients
            #Info messages are messages about connection status of clients

            message_decoded = message.decode(self.coding)

            if type == 'info':
                for client in self.clients:
                    client.send(message)

            elif type == 'msg':
                for client in self.clients:
                    now = datetime.now()
                    time = now.strftime("%H:%M:%S")
                    client.send(f'[{time}]{message_decoded}'.encode(self.coding))


    #Change accordingly to comment in __handle_cleint__(...)
    def __remove_client__(self,index):
        if self.clients[index] in self.clients:
            self.clients.remove(self.clients[index])
            self.nicknames.remove(self.nicknames[index])
            self.addresses.remove(self.addresses[index])
            self.threads.remove(self.threads[index])


    def __handle_client__(self,client):

        client_stop_condition = threading.Event()
        #Get index at this point and the nicknam since every client has its own thread
        index = self.clients.index(client)
        nickname = self.nicknames[index]

        while True:

            if client_stop_condition.is_set():
                print(f'{client} got disconnected.')
                self.__remove_client__(index)
                self.__broadcast_message__(f'{nickname} got disconnected from the server.'.encode(self.coding),'info')
                break

            try:
                message = client.recv(self.buffer)
                message_decoded = message.decode(self.coding)

                if message_decoded == '':
                    client_stop_condition.set()

                else:
                    self.__broadcast_message__(message,'msg')
            except:
                pass

    def server_start(self):
        self.server_socket.listen()
        print('Awaiting connections...')
        while True:
            try:
                client_socket, client_address = self.server_socket.accept()
                print(f'{client_socket} connected.')
                client_socket.send('N1CKN4M3'.encode(self.coding))
                client_nickname = client_socket.recv(self.buffer).decode(self.coding)

                self.__broadcast_message__(f'{client_nickname} just connected to a server.'.encode(self.coding),'info')

                self.clients.append(client_socket)
                self.addresses.append(client_address)
                self.nicknames.append(client_nickname)

                client_socket.send(f'Hi {client_nickname}, welcome to the server.'.encode(self.coding))

                client_thread = threading.Thread(target=self.__handle_client__,args=(client_socket,))
                client_thread.start()
                if client_thread not in self.threads:
                    self.threads.append(client_thread)

            except KeyboardInterrupt:
                self.server_socket.close()
                print('\nServer application terminated by keyboard interrupt.')
                break

#The lines below makes sure that the code in this file will only be executed when this file is run directly, useful in the case of importing this file as a module
def main():
    server = Server(4,'TCP','127.0.0.1',55555)
    server.server_start()

if __name__ == '__main__':
    main()