import socket
 
 
TCP_IP = '127.0.0.1'            # Local-host address (loop-back address, that is - I'm sending to myself).
TCP_PORT = 8888
BUFFER_SIZE = 1024
MESSAGE = "SIMPLE TIME"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Creates a default TCP socket.
s.connect((TCP_IP, TCP_PORT))   # Connects created socket with a server on the specified 
                                # address and the port.
s.send(MESSAGE)                 # Socket sends message on the previously established connection.
data = s.recv(BUFFER_SIZE)      # Socket receives a message from the server.
s.close()                       # TCP connection between the client's and server's sockets is closed.
 
print "received data:", data    
