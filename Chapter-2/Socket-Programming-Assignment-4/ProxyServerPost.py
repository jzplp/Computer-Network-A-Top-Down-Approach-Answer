# 找不到网站测试
#改为Python3格式
from socket import *
import sys
import os

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerPort = int(sys.argv[1])
tcpSerSock.bind(("", tcpSerPort))
print(tcpSerPort)
tcpSerSock.listen(10)
while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024)
    message = message.decode()
    print("message:", message)
    if(message == ''):
        continue
    # Extract the filename from the given message
    print("message.split()[1]:", message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print("filename:", filename)
    fileExist = "false"
    filetouse = "/" + filename
    print("filetouse:", filetouse)
    try:
        # Check wether the file exist in the cache
        f = open("WEB/" + filetouse[1:], "rb")
        outputdata = f.read()
        f.close()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.1 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
        tcpCliSock.send(outputdata)
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.","",1)
            print("hostn:", hostn)
            try:
                # Connect to the socket to port 80
                serverName = hostn.partition("/")[0]
                serverPort = 80
                print((serverName, serverPort))
                c.connect((serverName, serverPort))
                askFile = ''.join(filename.partition('/')[1:])
                print("askFile:", askFile)
                # Create a temporary file on this socket and ask port 80
                # for the file requested by the client
                fileobj = c.makefile('rwb', 0)
                if(message.split()[0] == 'GET'):
                    fileobj.write("GET ".encode() + askFile.encode() + " HTTP/1.0\r\nHost: ".encode() + serverName.encode() + "\r\n\r\n".encode())
                else: #POST
                    fileobj.write(
                        "POST ".encode() + askFile.encode() + " HTTP/1.0\r\nHost: ".encode() + serverName.encode() + "\r\n\r\n".encode())
                    fileobj.write(message.split("\r\n\r\n")[1].encode())
                # Read the response into buffer
                serverResponse = fileobj.read()
                if serverResponse.split()[0] != b'404':
                    print('404')
                    tcpCliSock.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
                    tcpCliSock.close()
                    continue
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                filename = "WEB/" + filename
                filesplit = filename.split('/')
                for i in range(0, len(filesplit) - 1):
                    if not os.path.exists("/".join(filesplit[0:i+1])):
                        os.makedirs("/".join(filesplit[0:i+1]))
                tmpFile = open(filename, "wb")
                print(serverResponse)
                serverResponse = serverResponse.split(b'\r\n\r\n')[1]
                print(serverResponse)
                tmpFile.write(serverResponse)
                tmpFile.close()
                tcpCliSock.send("HTTP/1.1 200 OK\r\n".encode())
                tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
                tcpCliSock.send(serverResponse)
            except:
                print("Illegal request")
            c.close()
        else:
            # HTTP response message for file not found
            print("NET ERROR")
    # Close the client and the server sockets
    tcpCliSock.close()
tcpSerSock.close()