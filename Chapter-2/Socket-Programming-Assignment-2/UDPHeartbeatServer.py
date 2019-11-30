#改为Python3格式
# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import time
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    message, address = serverSocket.recvfrom(1024)
    message = message.decode()
    message = message.split()[1]
    timeDiff = time.time() - float(message)
    print("receive RTT:", timeDiff)