"""
UDP Socket的客户端
环境 python3
"""

from socket import *

serverName = '49.52.10.72'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
# python3 改动
message = input("Input lowercase sentence:")
# python3 改动 socket要求byte类型数据
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage ,serverAddress = clientSocket.recvfrom(2048)
# python3 改动
print(modifiedMessage)

clientSocket.close()
