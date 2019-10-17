from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',1249))
s.listen(1)
conn,addr=s.accept()
while(1):
    m=conn.recv(1024)
    print(m.decode())
    ss=input()
    conn.send(ss.encode())