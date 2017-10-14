from datetime import datetime
import socket

HOST, PORT = '', 8888   # "HOST = ''" means the server is listening on all networking interfaces.

# The creation of the welcoming socket, and it's listening.
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

while True:
    client_connection, client_address = listen_socket.accept()  # TCP connection with a client established.
    request = client_connection.recv(1024)
    print request

    # Now, here am I a little confused.
    # "if" responds to a simple "SIMPLE TIME" request from the console.
    # "else" response is designed for a "browser" (HTTP) request, but it can be used for any client with a 
    # MESSAGE != "SIMPLE TIME", that is - where "if" condition is not satisfied.
    if request == "SIMPLE TIME":
        response = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    else:
        response = """\
HTTP/1.1 200 OK

%s u browseru""" % datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    client_connection.sendall(response)         # HTTP response sent.
    client_connection.close()                   # TCP connection closed.
