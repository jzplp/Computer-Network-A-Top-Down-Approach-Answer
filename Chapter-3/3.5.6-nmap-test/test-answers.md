
## 第三章 3.5.6节 关于nmap的小实验

实验环境：windows10

### 实验过程

1. windows没有nmap工具，需要手动下载：https://nmap.org/

2. 检测目标主机某端口的TCP是否开放  

* 无法到达指定的端口，可能是由于防火墙  
```
nmap -sT -p80 192.168.2.220
Starting Nmap 7.80 ( https://nmap.org ) at 2019-12-07 14:48 ?D1ú±ê×?ê±??
Nmap scan report for MI9-jzphone.lan (192.168.2.220)
Host is up (0.074s latency).

PORT   STATE    SERVICE
80/tcp filtered http
MAC Address: A8:9C:ED:A7:D9:EC (Xiaomi Communications)

Nmap done: 1 IP address (1 host up) scanned in 2.33 seconds
```

* 端口打开
```
nmap -sT -p80 192.168.2.1
Starting Nmap 7.80 ( https://nmap.org ) at 2019-12-07 14:51 ?D1ú±ê×?ê±??
Nmap scan report for phicomm.me (192.168.2.1)
Host is up (0.0024s latency).

PORT   STATE SERVICE
80/tcp open  http
MAC Address: 68:DB:54:CC:6B:BE (Phicomm (Shanghai))

Nmap done: 1 IP address (1 host up) scanned in 1.47 seconds
```

* 端口关闭
```
nmap -sT -p80 192.168.2.239
Starting Nmap 7.80 ( https://nmap.org ) at 2019-12-07 14:56 ?D1ú±ê×?ê±??
Nmap scan report for LAPTOP-3CP7H0GM.lan (192.168.2.239)
Host is up (1.0s latency).

PORT   STATE  SERVICE
80/tcp closed http

Nmap done: 1 IP address (1 host up) scanned in 3.38 seconds
```
必须关闭防火墙，才能检测到closed状态。  