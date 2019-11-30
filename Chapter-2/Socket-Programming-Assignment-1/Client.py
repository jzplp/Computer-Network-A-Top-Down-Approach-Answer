#Python3格式

from socket import *

serverName = '127.0.0.1'
serverPort = 80
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
outputdata = 'GET /hello.html HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n'
clientSocket.send(outputdata.encode())
data = 1
while data:
    data = clientSocket.recv(1024)
    print(data.decode(), end = '')
clientSocket.close()
