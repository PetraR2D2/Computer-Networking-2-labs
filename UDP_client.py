
from socket import *

server_name = "127.0.0.1"
server_port = 8000
client_socket = socket(AF_INET, SOCK_DGRAM)
modified_message = ""


while modified_message != "Kill":
    message = raw_input("Enter text: ")
    client_socket.sendto(message, (server_name, server_port))
    modified_message, server_address = client_socket.recvfrom(2048)
    print "Recieved from server: " + modified_message
client_socket.close()