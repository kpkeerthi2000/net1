import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = input("host")
port = int(input("enter a port num : "))
s.sendto(host.encode(),('127.0.0.1',port))


