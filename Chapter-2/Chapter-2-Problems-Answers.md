* **P1**  
a.错，应该发送4个请求报文。  
b.对。  
c.错。只能携带一个。  
d.错，Date首部表示服务器产生并发送响应报文的时间。  
e.错，例如在条件GET方法中，若对象没有被修改过，服务器返回的响应报文的报文体就是空的。  

* **P2**  
1. ACCESS CONTROL COMMANDS  
USER NAME (USER)  
PASSWORD (PASS)  
ACCOUNT (ACCT)  
CHANGE WORKING DIRECTORY (CWD)  
CHANGE TO PARENT DIRECTORY (CDUP)  
STRUCTURE MOUNT (SMNT)  
REINITIALIZE (REIN)  
LOGOUT (QUIT)  
2. TRANSFER PARAMETER COMMANDS  
DATA PORT (PORT)  
PASSIVE (PASV)  
REPRESENTATION TYPE (TYPE)  
FILE STRUCTURE (STRU)  
TRANSFER MODE (MODE)  
3. FTP SERVICE COMMANDS  
RETRIEVE (RETR)  
STORE (STOR)  
STORE UNIQUE (STOU)  
APPEND (with create) (APPE)  
ALLOCATE (ALLO)  
RESTART (REST)  
RENAME FROM (RNFR)  
RENAME TO (RNTO)  
ABORT (ABOR)  
DELETE (DELE)  
REMOVE DIRECTORY (RMD)  
MAKE DIRECTORY (MKD)  
PRINT WORKING DIRECTORY (PWD)  
LIST (LIST)  
NAME LIST (NLST)  
SITE PARAMETERS (SITE)  
SYSTEM (SYST)  
STATUS (STAT)  
HELP (HELP)  
NOOP (NOOP)  

* **P3**  
需要运输层协议 UDP TCP  
需要应用层协议 DNS  

* **P4**  
a. 文档的URL是 gaia.cs.umass.edu/cs453/index.html  
b. HTTP/1.1版本  
c. 持续连接  
d. 报文中并未提供IP地址  
e. 浏览器类型是Mozilla/5.0  
附带浏览器类型可以让服务器为不同的浏览器发送不同的版本。

* **P5**  
a. 找到了文档。回答的时间为：Tue, 07 Mar 2008 12:39:45 GMT  
b. 文档的时间为：SAT, 10 Dec2005 18:27:46 GMT  
c. 返回的字节数为3874  
d. 前五个字节： <!doc  
同意持续连接

* **P6**  
a.  
除非请求的Connect头域中包含了"close"标签，HTTP/1.1服务器总可以假定HTTP/1.1 客户端想要维持持续连接（persistent connection）。如果服务器想在发出响应后立即关闭连接，它应当发送一个含”close”的Connect头域。  
一个HTTP/1.1客户端可能期望保持连接一直开着，但这必须是基于服务器响应里是否包含一个Connect头域并且此头域里是否包含”close”。如果客户端不想为更多的请求维持连接，它应该发送一个值为”close”的Connect头域。  
如果客户端和服务器之一在发送的Connect头域里包含”close”，那么客户端的请求将会变为此连接的最后一个请求。  
因此，客户或者服务器都能发送信令通知连接关闭了。  
b.  
HTTP协议本身没有加密服务。  
c.  
不可以，最多两条并发持续连接。  
d.  
一方已经关闭，另一方通过连接传输数据是不可能的。  
因此要求客户端软件应该能重新打开传输层连接并重新传输遗弃的请求序列而不需要用户进行交互来实现。  

* **P7**  
时间为：2RTT<sub>0</sub>+RTT<sub>1</sub>+...+RTT<sub>n</sub>

* **P8**  
a. 18RTT<sub>0</sub>+RTT<sub>1</sub>+...+RTT<sub>n</sub>  
b. 6RTT<sub>0</sub>+RTT<sub>1</sub>+...+RTT<sub>n</sub>  
c. 3RTT<sub>0</sub>+RTT<sub>1</sub>+...+RTT<sub>n</sub>  

* **P9**  
a.  
850000b = 0.85Mb  
Δ = 0.85Mb/15Mbps = 0.0567s  
β = 16/s  
平均接入时延 = 0.0567/(1-0.0567 * 16) = 0.611s  
总平均响应时间 = 3+0.611 =3.611s  
b.  
β = 16 * 0.6 = 9.6/s  
平均接入时延 = 0.0567/(1-0.0567 * 9.6) = 0.124s  
命中时的总响应时间 = 0.85Mb/100Mbps = 0.0085s  
非命中时的总的平均响应时间 = 3 + 0.124 = 3.124s  
总的平均响应时间 = 0.0085 * 0.4 + 3.124 * 0.6 = 0.0034 + 1.8744 = 1.8778s

* **P10**  
总共包含一个初始对象和10个引用的对象。  
仅考虑独占时通过短链路的时间。  
一个控制分组通过短链路的时间为：  
t1 = 200/150 = 1.33s  
一个数据分组通过短链路的时间。  
t2 = 100k/150= 666.67s  
如果采用非持续HTTP的并行下载：  
下载初始对象时，独占短链路，时间为 3 * t1 + t2 = 670.66s  
同时下载10个引用对象，每个连接获得的1/10的链路带宽。   
由于数据分组长度相同，控制分组长度也相同，而且平均分配带宽，因此时间相同。  
(3 * t1 + t2 ) * 10 = 6706.6s  
总时间为 7377.26s  
如果采用持续HTTP的下载：  
下载初始对象时，独占短链路，时间为 3 * t1 + t2 = 670.66s   
依次下载10个引用对象，由于不需要握手，只需要发送10个请求分组，而且连续发送，不需要均分带宽。  
（t1 + t2） * 10 = 6680s  
总时间为 7350.66s  
实际时间差距约为27s，也就少发了几条控制分组，相比总时间，基本没有减小。  
