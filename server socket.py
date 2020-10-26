import socket

my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 8080
my_server.bind((host,port))
my_server.listen(5)

while True:
    conn, address = my_server.accept()
    print("connected by",address)
    data = conn.recv(4000)
    print("recieved data:",data)
    conn.send(b"I am your server")
    conn.close()
    print("Client Disconnect")




