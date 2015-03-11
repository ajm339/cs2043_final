# import SocketServer

# class MyUDPHandler(SocketServer.BaseRequestHandler):
#     """
#     This class works similar to the TCP handler class, except that
#     self.request consists of a pair of data and client socket, and since
#     there is no connection the client address must be given explicitly
#     when sending data back via sendto().
#     """

#     def handle(self):
#         data = self.request[0].strip()
#         socket = self.request[1]
#         print "{} wrote:".format(self.client_address[0])
#         print data
#         socket.sendto(data.upper(), self.client_address)

# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999
#     server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
#     server.serve_forever()



# Echo server program
import socket
HOST = ''      # Symbolic name meaning the local host
PORT = 5006  # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print 'hi'
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    print 'hi'
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()
print 'close'