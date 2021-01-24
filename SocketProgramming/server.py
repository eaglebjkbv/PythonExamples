import socket



s = socket.socket()
host = socket.gethostname()
port = 3333
s.bind((host, port))

s.listen()
while True:

    c, addr = s.accept()
    
    print(addr, " Adresinden Bağlandı")
    c.send(b"Selamlar")
    c.close()
