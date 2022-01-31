
import socket

# by default IPv4 and TCP
s = socket.socket()

print("socket created")

# binding a socket with a port number
s.bind(('localhost', 16345))

# no.of connections
s.listen(3)
print('waiting for connections')

while True:
    c, address = s.accept()

    name = c.recv(1024).decode()
    print("connected with ", address, name)

    c.send(bytes('welcome client','utf-8'))

    c.close()
