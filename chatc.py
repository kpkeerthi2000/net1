from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',1249))
while(1):
    msg=input()
    s.send(msg.encode())
    b=s.recv(1024).decode()
    print(b)