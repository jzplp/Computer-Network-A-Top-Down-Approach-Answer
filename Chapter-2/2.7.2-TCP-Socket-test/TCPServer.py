"""
TCP Socket的服务器端
环境 python3
"""

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
# python3 改动
print("The server is ready to receive")
while 1:
    connectSocket , addr = serverSocket.accept()
    sentence = connectSocket.recv(1024)
    capitalizeSentence =sentence.upper()
    connectSocket.send(capitalizeSentence)
    connectSocket.close()
