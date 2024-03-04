import socket

s = socket.socket()

s.bind(('localhost', 9999))

s.listen(3)
print("Waiting for connections...")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with " + name + " at", addr )
    c.send(bytes('Welcome ' + name + ' to my server', 'utf-8'))
    c.close()