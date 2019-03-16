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