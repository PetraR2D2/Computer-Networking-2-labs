from datetime import datetime   # Used to fetch the time as a server's response to client's request
import socket

HOST, PORT = '', 8888   # HOST = '' means the server is listening on all networking interfaces

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    if request == "SIMPLE TIME":    
        http_response = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    else:
        http_response = """\
HTTP/1.1 200 OK

%s""" % datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    client_connection.sendall(http_response)
    client_connection.close()