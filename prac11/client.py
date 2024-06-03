import socket

c=socket.socket()
host=socket.gethostname()
c.connect((host,3000))
print(c.recv(1024).decode())
while(True):
    c.send(input("Enter your message: ").encode())
    print(c.recv(1024).decode())