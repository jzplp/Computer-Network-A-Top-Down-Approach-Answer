#改为Python3格式
#import socket module
from socket import *
import threading
def webProcess(connectionSocket):
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:], "rb")
        outputdata = f.read()
        outputdata = outputdata.decode()
        f.close()
        #Send one HTTP header line into socket
        outputdata = 'HTTP/1.1 200 OK\r\n\r\n' + outputdata
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
        print("OK!")
    except IOError:
        #Send response message for file not found
        outputdata = 'HTTP/1.1 404 Not Found\r\n\r\n'
        #Close client socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 80
serverSocket.bind(("", serverPort))
serverSocket.listen(10)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target = webProcess, args = (connectionSocket, ))
    thread.start()
serverSocket.close()
