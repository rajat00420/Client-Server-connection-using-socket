import socket

my_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '' #your ip ipv4 ip address which can be checked using ipconfig#
port = 8080
my_client.connect((host,port))


my_client.send(b"hello i am rajat\n")

recv = my_client.recv(4000)
print("recieved",recv)
print("connection recieved")
