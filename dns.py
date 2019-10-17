from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',1234))
s.listen(1)
ip=gethostbyname('www.google.com')
c,addr=s.accept()
c.send(ip.encode())
#print(ip)

