import socket
import threading

class Client:

    nickname = ''

    received = ''
    sent = ''

    coding = 'utf-8'
    buffer = 1024 #Need to think about the case very sent message is over the buffer size

    #There may be some redundancy in checking whether the ipv4 address is correct
    def __check_ipv4__(ip_address):

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
    def __check_port_number__(port_number):

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
    def __init__(self,ip_version,transport_protocol):
        
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
        
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        Client.nickname = input('What is your nickname: ')
    
    def __receive_message__(self):
        while True:
            try:
                Client.received = Client.client_socket.recv(Client.buffer).decode(Client.coding)
                print(Client.received)
            except:
                pass

    def __send_message__(self):
        while True:
            try:
                if Client.received == 'N1CKN4ME':
                    Client.client_socket.send(Client.nickname.encode(Client.coding))
                else:
                    Client.sent = input()
                    Client.client_socket.send(Client.sent.encode(Client.coding))
            except:
                pass

    def connect_to_server(self,ip_address,port_number):
        
        if self.ip_version == 4:
            if Client.__check_ipv4__(ip_address) == -1 or Client.__check_port_number__(port_number) == -1:
                return
            else:
                try:
                    self.client_socket.connect((ip_address,port_number))
                except:
                    print('Unable to establish connection with the server.')
                    return

        check = self.client_socket.recv(Client.buffer).decode(Client.coding)
        print(check)

        #receive_thread = threading.Thread(target=Client.__receive_message__,args=(self,))
        #receive_thread.start()
#
        #send_thread = threading.Thread(target=Client.__send_message__,args=(self,))
        #send_thread.start()

#The lines below makes sure that the code in this file will only be executed when this file is run directly, useful in the case of importing this file as a module
def main():
    client = Client(4,'TCP')
    client.connect_to_server('127.0.0.1',55555)

if __name__ == '__main__':
    main()