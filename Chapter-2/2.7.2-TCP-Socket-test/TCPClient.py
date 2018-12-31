"""
TCP Socket的客户端
环境 python3
"""

from socket import *

serverName = '49.52.10.72'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# python3 改动
sentence = input("Input lowercase sentence:")
# python3 改动 socket要求byte类型数据
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
# python3 改动
print("From Server:" + modifiedSentence.decode())
clientSocket.close()
