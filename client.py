import socket

c = socket.socket()

# enter server's ip address instead localhost when you run this on other machine
c.connect(('localhost',16345))

name = input("enter ur name")
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())

