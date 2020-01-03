# 对代码进行了少部分改动

import socket
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8


def checksum(strCheck):
    csum = 0
    countTo = (len(strCheck) / 2) * 2
    count = 0
    while count < countTo:
        thisVal = strCheck[count + 1] * 256 + strCheck[count]
        csum = csum + thisVal
        csum = csum & 0xffffffff
        count = count + 2

    if countTo < len(strCheck):
        csum = csum + strCheck[len(strCheck) - 1]
        csum = csum & 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout

    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:  # Timeout
            return "Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)

        header = recPacket[20:28]
        header_type, header_code, header_checksum, header_packet_ID, header_sequence = struct.unpack("bbHHh", header)

        if(header_type != 0 or header_code != 0 or header_packet_ID != ID or header_sequence != 1):
            if(header_type == 3 and header_code == 0):
                return "目的网络不可达"
            if(header_type == 3 and header_code == 1):
                return "目的主机不可达"
            if(header_type == 3 and header_code == 2):
                return "目的协议不可达"
            if(header_type == 3 and header_code == 3):
                return "目的端口不可达"
            if(header_type == 3 and header_code == 6):
                return "目的网络未知"
            if(header_type == 3 and header_code == 7):
                return "目的主机未知"
            if(header_type == 4 and header_code == 0):
                return "源抑制"
            if(header_type == 12 and header_code == 0):
                return "IP首部损坏"
            return "Request error."

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return "Request timed out."
        return 1 - timeLeft


def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)

    myChecksum = 0
    # Make a dummy header with a 0 checksum.
    # 创建一个带有0校验和的伪头。
    # struct -- Interpret strings as packed binary data
    # struct-将字符串解释为打包的二进制数据
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    # Calculate the checksum on the data and the dummy header.
    # 计算数据和虚拟头的校验和。
    myChecksum = checksum(header + data)

    # Get the right checksum, and put in the header
    if sys.platform == 'darwin':
        myChecksum = socket.htons(myChecksum) & 0xffff
        # Convert 16-bit integers from host to network byte order.
        # 将主机的16位整数转换为网络字节顺序。
    else:
        myChecksum = socket.htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data

    mySocket.sendto(packet, (destAddr, 1))  # AF_INET address must be tuple, not str
    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object


def doOnePing(destAddr, timeout):
    icmp = socket.getprotobyname("icmp")

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

    myID = os.getpid() & 0xFFFF  # Return the current process i
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)

    mySocket.close()
    return delay


def ping(host, timeout=1):
    # timeout=1 means: If one second goes by without a reply from the server,
    # the client assumes that either the client’s ping or the server’s pong is lost
    # timeout = 1 表示：如果一秒钟没有收到服务器的答复，则客户端会认为客户端的ping或服务器的pong丢失了
    dest = socket.gethostbyname(host)
    print("正在 Ping", host, "[", dest, "] :")
    # Send ping requests to a server separated by approximately one second
    # 将ping请求发送到间隔约一秒钟的服务器
    num = 4
    lost = 0
    delayList = []
    for i in range(num):
        delay = doOnePing(dest, timeout)
        if(type(delay) == str):
            print(delay)
            lost = lost + 1
            continue
        delay = int(delay * 1000)
        delayList.append(delay)
        print("来自", dest, "的回复: 时间=", delay, "ms")
        time.sleep(1)  # one second
    print(dest, "的 Ping 统计信息:")
    print("\t数据包: 已发送 =", num, "，已接收 =", num - lost, "，丢失 =", lost, "(", lost/num * 100, "% 丢失)")
    if(delayList):
        print("往返行程的估计时间(以毫秒为单位):")
        print("\t最短 =", min(delayList), "ms，最长 =", max(delayList), "ms，平均 =", sum(delayList)/len(delayList), "ms")

ping("www.12306.cn")