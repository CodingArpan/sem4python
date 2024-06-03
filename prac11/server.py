import socket

s = socket.socket()
host = socket.gethostname()
port = 3000
s.bind((host, port))
print("Server is running on port:", port)
s.listen(2)
while (True):
    conn, addr = s.accept()
    print("Connection from:", addr)
    conn.send("connected to server".encode())
    while (True):
        print(conn.recv(1024).decode())
        conn.send(input("Enter your message: ").encode())
