#改为Python3格式
from socket import *
import base64
import ssl

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.163.com"
mailUser = 'jz163wy'
mailFromAddress = 'jz163wy@163.com'
mailPassWord = '******'
mailToAddress = 'ecnujz@qq.com'

msg = 'FROM: ' + mailFromAddress + '\r\n'
msg += 'TO: ' + mailToAddress +  '\r\n'
msg += 'Subject: ' + 'test' +  '\r\n'
msg += "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Create socket called clientSocket and establish a TCP connection with mailserver
context = ssl.create_default_context()
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 465))
clientSocketSSL = context.wrap_socket(clientSocket, server_hostname=mailserver)

recv = clientSocketSSL.recv(1024)
recv = recv.decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO mailserver\r\n'
while True:
    clientSocketSSL.send(heloCommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# 登录过程
loginCommand = 'auth login\r\n'
while True:
    clientSocketSSL.send(loginCommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '334':
        break

# 邮箱账户经过base64编码
userCommand = base64.b64encode(mailUser.encode()) + b'\r\n'
while True:
    clientSocketSSL.send(userCommand)
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '334':
        break

# 邮箱密码经过base64编码 这里不展示密码了
passCommand = base64.b64encode(mailPassWord.encode()) + b'\r\n'
while True:
    clientSocketSSL.send(passCommand)
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '235':
        break

# Send MAIL FROM command and print server response.
MFCommand = 'MAIL FROM: <'+ mailFromAddress + '>\r\n'
while True:
    clientSocketSSL.send(MFCommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send RCPT TO command and print server response.
RTCommand = 'RCPT TO: <'+ mailToAddress + '>\r\n'
while True:
    clientSocketSSL.send(RTCommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send DATA command and print server response.
DATACommand = 'DATA\r\n'
while True:
    clientSocketSSL.send(DATACommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '354':
        break

# Send message data.
clientSocketSSL.send(msg.encode())

# Message ends with a single period.
while True:
    clientSocketSSL.send(endmsg.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send QUIT command and get server response.
QUITCommand = 'QUIT\r\n'
while True:
    clientSocketSSL.send(QUITCommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '221':
        break

clientSocketSSL.close()
