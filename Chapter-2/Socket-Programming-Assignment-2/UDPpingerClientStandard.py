# UDPPingerClient.py
from socket import *
import time
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
print("正在Ping", serverName, "数据:")
receNum = 0
MaxDiffTime = -1
MinDiffTime = 2
AverDiffTime = 0
for i in range(10):
    time1 = time.time()
    outputdata = 'Ping ' + str(i) + " " + str(time1)
    # 设置超时 单位秒
    clientSocket.settimeout(1)
    clientSocket.sendto(outputdata.encode(), (serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        timeDiff = time.time() - time1
        print("来自", serverName, "的回复：字节=", str(len(outputdata)), "RTT:", str(timeDiff))
        receNum += 1
        AverDiffTime += timeDiff
        if(timeDiff > MaxDiffTime):
            MaxDiffTime = timeDiff
        if (timeDiff < MinDiffTime):
            MinDiffTime = timeDiff
    except:
        print("请求超时")
print(serverName, "的 Ping 统计信息:")
print("\t数据包: 已发送 = 10 已接收 =", str(receNum), "丢失 =", str(10-receNum), "(", str(int((10-receNum)*100/receNum)), "% 丢失)" )
if(receNum != 0):
    print("往返行程的估计时间(以秒为单位):")
    print("\t最短 =", MinDiffTime, "最长 =", MaxDiffTime, "平均 =", AverDiffTime/receNum)
