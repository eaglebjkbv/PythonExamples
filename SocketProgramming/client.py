import socket


s = socket.socket()
host = socket.gethostname()
port = 3333

s.connect((host, port))
print("Gelen Data", s.recv(1024))
s.close()
