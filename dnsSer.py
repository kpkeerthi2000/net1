import socket   
import os
import sys 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port= int(input("enter port num : "))

s.bind(('127.0.0.1',port))
conn , addr = s.recvfrom(512)
print(socket.gethostbyname(conn.decode()))


