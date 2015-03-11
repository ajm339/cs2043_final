# import socket
# import sys

# HOST, PORT = "localhost", 4000
# data = "alex".join(sys.argv[1:])

# # SOCK_DGRAM is the socket type to use for UDP sockets
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # As you can see, there is no connect() call; UDP has no connections.
# # Instead, data is directly sent to the recipient via sendto().
# sock.sendto(data + "\n", (HOST, PORT))
# received = sock.recv(1024)

# print "Sent:     {}".format(data)
# print "Received: {}".format(received)


import socket

HOST = ""
PORT = 5006
message = "WIN"

print "HOST:", HOST
print "PORT:", PORT
print "message:", message

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message, (HOST, PORT))