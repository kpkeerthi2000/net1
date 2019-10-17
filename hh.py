import socket


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 12345))
serversocket.listen(1)

msg = """
HTTP/1.1
Content-Type: text/html

<html>
<body>
<b>Hello World</b>
</body>
</html>

"""

(clientsocket, address) = serversocket.accept()
clientsocket.send(msg.encode())
a=input()
