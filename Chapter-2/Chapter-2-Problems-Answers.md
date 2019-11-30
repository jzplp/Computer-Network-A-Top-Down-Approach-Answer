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

* **P11**  
a.  
下载一个初试对象时，Bob和其它4个用户时间相同每个用户独占1/5带宽。  
时间为 (3 * t1 + t2) * 5 = 3353.3s  
下载10个引用对象时，Bob打开10个HTTP并行连接，其他用户分别打开1个连接。每个连接占1/14的带宽.  
Bob下载的时间为：  
(3 * t1 + t2) * 14 = 9389.24s  
此时其他用户仅仅下载完一个引用对象，并继续下载其余对象，每个占用1/4带宽。  
(3 * t1 + t2) * 4 * 9 = 24143.76s  
Bob花费的总时间为 12742.54s  
其他用户花费的总时间为 36886.3s  
因此，Bob的并行连接可以帮助他更快的得到Web页面。  
b.  
如果其它用户采用并行下载，而Bob不采用，那么Bob将比其他用户获得更少的带宽。因此并行连接依然是有益的。

* **P12**  
服务器程序代码：  
[Chapter-2/PA-P12/P12.py](PA-P12/P12.py)  
用Chrome浏览器进行测试，发现部分报文的含有条件GET。  

* **P13**  
MAIL FROM 是SMTP协议命令。From 不是。  
事实上不写From，邮件也可以正常发送。因此MAIL FROM更重要。

* **P14**  
SMTP  
是用一个单行的"."来标识报文体结束的。  
HTTP(来源于网络)  
如果是长连接(keep-alive),则有两种方式，一种是指示content-length,一种是用chunk传送。这两种都有办法知道包的结束。  
如果是短连接，socket连接断了，就是包的结束。  
HTTP如果采用SMTP的方法，大部分情况下也是没问题的。  

* **P15**  
MTA是邮件传输代理，负责邮件传输，把邮件交给MUA（邮件用户代理）。  
下面内容来源于网络：  
Received 是 在将消息转发到 Internet 环境或从 Internet 环境转发消息时，网关必须预先添加 Received 行，并且它不得以任何方式更改已在标题部分中的 Received 行。
因此排在最后面的 Received 行所指示的地址就是源地址，即 58.88.21.177

* **P16**  
UIDL的命令是给出信件数。  
下面摘自RFC1939  
【参数】信件数（可选）。如果给出信件数，不包括被标记为删除的信件。  
【限制】仅在 " 操作 " 状态下使用。  
【说明】  
如果给出了参数，且 POP3 服务器返回包括上述信息的 " 确认 " ，此行称为信息的 " 独立 -ID 表 " 。  
如果没有参数，服务器返回 " 确认 " 响应，此响应便以多行给出。在初的 +OK 后，对于每个信件，服务器均给出相应的响应。此行叫做信件的 " 独立 -ID 表 " 。  
为简化语法分析，所有服务器要求使用独立 -ID 表的特定格式。它包括空格和信件的独立 -ID 。  
信件的独立 -ID 由 0x21 到 0x7E 字符组成，这个符号在给定的存储邮件中不会重复。  
注意：信件不包括被标记为删除的信件。  
【响应】 +OK ：其后是独立 -ID 表；  
-ERR ：其后无类似信件。   

* **P17**  
a 和 b 略  
c. 对于保持模式，第一次和第二次的会话记录时相同的。会话记录为：
```
C: list
S: 1 489
S: 2 912
S: .
C: retr 1
S: blah blah ......
S: ....... blah
S: .
C: retr 2
S: blah blah ......
S: ....... blah
S: .
C: QUIT
S: +OK
```

* **P18**  
a.  
whois数据库是用来查询域名是否被注册和注册域名详细信息的数据库。  
b.  
```
whois baidu.com
WHOIS Server: whois.markmonitor.com
Name Server: ns4.baidu.com
Name Server: ns1.baidu.com
Name Server: ns3.baidu.com
Name Server: ns7.baidu.com
Name Server: ns2.baidu.com

whois qq.com
WHOIS Server: whois.markmonitor.com
Name Server: ns1.qq.com
Name Server: ns4.qq.com
Name Server: ns2.qq.com
Name Server: ns3.qq.com
```
c.  
```
nslookup
默认服务器:  moon.ecnu.edu.cn
Address:  202.120.80.2

nslookup ns1.qq.com
服务器:  moon.ecnu.edu.cn
Address:  202.120.80.2
非权威应答:
名称:    ns1.qq.com
Addresses:  183.3.226.207
          101.89.19.165
          157.255.246.101

nslookup ns1.baidu.com
服务器:  moon.ecnu.edu.cn
Address:  202.120.80.2
非权威应答:
名称:    ns1.baidu.com
Address:  202.108.22.220

nslookup -qt=A qq.com
服务器:  moon.ecnu.edu.cn
Address:  202.120.80.2
非权威应答:
名称:    qq.com
Addresses:  182.254.34.74
          182.254.74.167
          182.254.18.159

nslookup -qt=NS qq.com
服务器:  moon.ecnu.edu.cn
Address:  202.120.80.2
非权威应答:
qq.com  nameserver = ns3.qq.com
qq.com  nameserver = ns4.qq.com
qq.com  nameserver = ns2.qq.com
qq.com  nameserver = ns1.qq.com

nslookup -qt=CNAME qq.com
服务器:  moon.ecnu.edu.cn
Address:  202.120.80.2
qq.com
        primary name server = ns1.qq.com
        responsible mail addr = webmaster.qq.com
        serial  = 1330914143
        refresh = 3600 (1 hour)
        retry   = 300 (5 mins)
        expire  = 86400 (1 day)
        default TTL = 300 (5 mins)

nslookup -qt=MX qq.com
服务器:  moon.ecnu.edu.cn
Address:  202.120.80.2
非权威应答:
qq.com  MX preference = 10, mail exchanger = mx3.qq.com
qq.com  MX preference = 20, mail exchanger = mx2.qq.com
qq.com  MX preference = 30, mail exchanger = mx1.qq.com
```

d.  
c中的qq.com就有多个IP地址  
我所在的学校只有一个IP地址  
```
nslookup www.ecnu.edu.cn
服务器:  moon.ecnu.edu.cn
Address:  202.120.80.2
非权威应答:
名称:    imhttps.ecnu.edu.cn
Address:  202.120.88.27
Aliases:  www.ecnu.edu.cn
```

e.  
```
whois -s whois.arin.net 202.120.88.27
WHOIS Server: whois.arin.net
NetRange:       202.0.0.0 - 202.255.255.255
CIDR:           202.0.0.0/8
NetName:        APNIC-CIDR-BLK
```

f.  
利用nslookup和whois数据库确定一个机构的具体信息，各类服务器的地址  

g.  
因为公众访问网络时，有权利了解网站的相关信息，而且方便用户注册域名或者IP  

* **P19**  
a.  
```
dig www.ecnu.edu.cn +trace
; <<>> DiG 9.10.3-P4-Ubuntu <<>> www.ecnu.edu.cn +trace
;; global options: +cmd
.			5	IN	NS	j.root-servers.net.
.			5	IN	NS	b.root-servers.net.
.			5	IN	NS	i.root-servers.net.
.			5	IN	NS	f.root-servers.net.
.			5	IN	NS	l.root-servers.net.
.			5	IN	NS	c.root-servers.net.
.			5	IN	NS	a.root-servers.net.
.			5	IN	NS	g.root-servers.net.
.			5	IN	NS	d.root-servers.net.
.			5	IN	NS	m.root-servers.net.
.			5	IN	NS	h.root-servers.net.
.			5	IN	NS	k.root-servers.net.
.			5	IN	NS	e.root-servers.net.
;; Received 241 bytes from 127.0.1.1#53(127.0.1.1) in 3 ms

cn.			172800	IN	NS	a.dns.cn.
cn.			172800	IN	NS	b.dns.cn.
cn.			172800	IN	NS	c.dns.cn.
cn.			172800	IN	NS	d.dns.cn.
cn.			172800	IN	NS	e.dns.cn.
cn.			172800	IN	NS	f.dns.cn.
cn.			172800	IN	NS	g.dns.cn.
cn.			172800	IN	NS	ns.cernet.net.
后面忽略
;; Received 706 bytes from 198.97.190.53#53(h.root-servers.net) in 244 ms

edu.cn.			172800	IN	NS	dns2.edu.cn.
edu.cn.			172800	IN	NS	deneb.dfn.de.
edu.cn.			172800	IN	NS	ns2.cernet.net.
edu.cn.			172800	IN	NS	ns2.cuhk.hk.
edu.cn.			172800	IN	NS	dns.edu.cn.
后面忽略
;; Received 494 bytes from 202.112.0.44#53(ns.cernet.net) in 43 ms

ecnu.edu.cn.		172800	IN	NS	liwa.ecnu.edu.cn.
ecnu.edu.cn.		172800	IN	NS	xiayu.ecnu.edu.cn.
后面忽略
;; Received 413 bytes from 137.189.6.21#53(ns2.cuhk.hk) in 54 ms

www.ecnu.edu.cn.	3600	IN	CNAME	imhttps.ecnu.edu.cn.
imhttps.ecnu.edu.cn.	3600	IN	A	202.120.88.27
;; Received 82 bytes from 202.120.80.1#53(liwa.ecnu.edu.cn) in 4 ms
```

b.  
```
dig www.google.com +trace
; <<>> DiG 9.10.3-P4-Ubuntu <<>> www.google.com +trace
;; global options: +cmd
.			5	IN	NS	l.root-servers.net.
.			5	IN	NS	c.root-servers.net.
.			5	IN	NS	h.root-servers.net.
.			5	IN	NS	a.root-servers.net.
.			5	IN	NS	j.root-servers.net.
.			5	IN	NS	g.root-servers.net.
.			5	IN	NS	e.root-servers.net.
.			5	IN	NS	b.root-servers.net.
.			5	IN	NS	m.root-servers.net.
.			5	IN	NS	i.root-servers.net.
.			5	IN	NS	f.root-servers.net.
.			5	IN	NS	d.root-servers.net.
.			5	IN	NS	k.root-servers.net.
;; Received 241 bytes from 127.0.1.1#53(127.0.1.1) in 3 ms

com.			172800	IN	NS	c.gtld-servers.net.
com.			172800	IN	NS	k.gtld-servers.net.
com.			172800	IN	NS	g.gtld-servers.net.
com.			172800	IN	NS	d.gtld-servers.net.
com.			172800	IN	NS	h.gtld-servers.net.
com.			172800	IN	NS	b.gtld-servers.net.
com.			172800	IN	NS	j.gtld-servers.net.
com.			172800	IN	NS	e.gtld-servers.net.
com.			172800	IN	NS	i.gtld-servers.net.
com.			172800	IN	NS	l.gtld-servers.net.
com.			172800	IN	NS	m.gtld-servers.net.
com.			172800	IN	NS	a.gtld-servers.net.
com.			172800	IN	NS	f.gtld-servers.net.
后面忽略
;; Received 1174 bytes from 192.112.36.4#53(g.root-servers.net) in 13 ms

www.google.com.		240	IN	A	69.171.224.85
;; Received 59 bytes from 192.54.112.30#53(h.gtld-servers.net) in 29 ms

dig www.yahoo.com +trace
; <<>> DiG 9.10.3-P4-Ubuntu <<>> www.yahoo.com +trace
;; global options: +cmd
.			5	IN	NS	h.root-servers.net.
.			5	IN	NS	m.root-servers.net.
.			5	IN	NS	e.root-servers.net.
.			5	IN	NS	i.root-servers.net.
.			5	IN	NS	k.root-servers.net.
.			5	IN	NS	a.root-servers.net.
.			5	IN	NS	l.root-servers.net.
.			5	IN	NS	f.root-servers.net.
.			5	IN	NS	c.root-servers.net.
.			5	IN	NS	d.root-servers.net.
.			5	IN	NS	j.root-servers.net.
.			5	IN	NS	b.root-servers.net.
.			5	IN	NS	g.root-servers.net.
;; Received 241 bytes from 127.0.1.1#53(127.0.1.1) in 3 ms

com.			172800	IN	NS	f.gtld-servers.net.
com.			172800	IN	NS	e.gtld-servers.net.
com.			172800	IN	NS	b.gtld-servers.net.
com.			172800	IN	NS	i.gtld-servers.net.
com.			172800	IN	NS	h.gtld-servers.net.
com.			172800	IN	NS	l.gtld-servers.net.
com.			172800	IN	NS	m.gtld-servers.net.
com.			172800	IN	NS	g.gtld-servers.net.
com.			172800	IN	NS	j.gtld-servers.net.
com.			172800	IN	NS	a.gtld-servers.net.
com.			172800	IN	NS	d.gtld-servers.net.
com.			172800	IN	NS	c.gtld-servers.net.
com.			172800	IN	NS	k.gtld-servers.net.
后面忽略
;; Received 1173 bytes from 199.7.91.13#53(d.root-servers.net) in 30 ms

yahoo.com.		172800	IN	NS	ns1.yahoo.com.
yahoo.com.		172800	IN	NS	ns5.yahoo.com.
yahoo.com.		172800	IN	NS	ns2.yahoo.com.
yahoo.com.		172800	IN	NS	ns3.yahoo.com.
yahoo.com.		172800	IN	NS	ns4.yahoo.com.
后面忽略
;; Received 845 bytes from 192.35.51.30#53(f.gtld-servers.net) in 224 ms

www.yahoo.com.		1800	IN	CNAME	atsv2-fp-shed.wg1.b.yahoo.com.
wg1.b.yahoo.com.	172800	IN	NS	yf1.yahoo.com.
wg1.b.yahoo.com.	172800	IN	NS	yf2.yahoo.com.
wg1.b.yahoo.com.	172800	IN	NS	yf3.a1.b.yahoo.net.
wg1.b.yahoo.com.	172800	IN	NS	yf4.a1.b.yahoo.net.
;; Received 194 bytes from 98.138.11.157#53(ns4.yahoo.com) in 261 ms

dig www.amazon.com +trace
; <<>> DiG 9.10.3-P4-Ubuntu <<>> www.amazon.com +trace
;; global options: +cmd
.			5	IN	NS	a.root-servers.net.
.			5	IN	NS	i.root-servers.net.
.			5	IN	NS	e.root-servers.net.
.			5	IN	NS	d.root-servers.net.
.			5	IN	NS	l.root-servers.net.
.			5	IN	NS	j.root-servers.net.
.			5	IN	NS	g.root-servers.net.
.			5	IN	NS	c.root-servers.net.
.			5	IN	NS	h.root-servers.net.
.			5	IN	NS	k.root-servers.net.
.			5	IN	NS	m.root-servers.net.
.			5	IN	NS	b.root-servers.net.
.			5	IN	NS	f.root-servers.net.
;; Received 241 bytes from 127.0.1.1#53(127.0.1.1) in 8 ms

com.			172800	IN	NS	b.gtld-servers.net.
com.			172800	IN	NS	i.gtld-servers.net.
com.			172800	IN	NS	j.gtld-servers.net.
com.			172800	IN	NS	c.gtld-servers.net.
com.			172800	IN	NS	f.gtld-servers.net.
com.			172800	IN	NS	d.gtld-servers.net.
com.			172800	IN	NS	g.gtld-servers.net.
com.			172800	IN	NS	h.gtld-servers.net.
com.			172800	IN	NS	k.gtld-servers.net.
com.			172800	IN	NS	e.gtld-servers.net.
com.			172800	IN	NS	l.gtld-servers.net.
com.			172800	IN	NS	a.gtld-servers.net.
com.			172800	IN	NS	m.gtld-servers.net.
后面忽略
;; Received 1174 bytes from 199.9.14.201#53(b.root-servers.net) in 243 ms

amazon.com.		172800	IN	NS	pdns1.ultradns.net.
amazon.com.		172800	IN	NS	pdns6.ultradns.co.uk.
amazon.com.		172800	IN	NS	ns1.p31.dynect.net.
amazon.com.		172800	IN	NS	ns3.p31.dynect.net.
amazon.com.		172800	IN	NS	ns2.p31.dynect.net.
amazon.com.		172800	IN	NS	ns4.p31.dynect.net.
后面忽略
;; Received 741 bytes from 192.35.51.30#53(f.gtld-servers.net) in 198 ms

www.amazon.com.		1800	IN	CNAME	www.cdn.amazon.com.
cdn.amazon.com.		900	IN	NS	ns-61.awsdns-07.com.
cdn.amazon.com.		900	IN	NS	ns-1136.awsdns-14.org.
cdn.amazon.com.		900	IN	NS	ns-1894.awsdns-44.co.uk.
cdn.amazon.com.		900	IN	NS	ns-774.awsdns-32.net.
;; Received 205 bytes from 204.74.108.1#53(pdns1.ultradns.net) in 254 ms
```

* **P20**  
在不同的时间点多次采样缓存，看看缓存中哪些Web服务器出现的机率更大。

* **P21**  
不会做。

* **P22**  
客户-服务器分发 

|  | N = 10 | N = 100 | N = 1000 |
| :---: | :---: | :---: | :---: |
| u = 300kbps | 7500 | 50000 | 500000 |
| u = 700kbps | 7500 | 50000 | 500000 |
| u = 2Mbps | 7500 | 50000 | 500000 |

P2P分发 

|  | N = 10 | N = 100 | N = 1000 |
| :---: | :---: | :---: | :---: |
| u = 300kbps | 7500 | 25000 | 45455 |
| u = 700kbps | 7500 | 15000 | 20548 |
| u = 2Mbps | 7500 | 7500 | 7500 |

* **P23**  
a.  
向每个对等方以u<sub>s</sub>/N的速率传输，每个对等方同时收到完整文件，时间为NF/u<sub>s</sub>  
b.  
向d<sub>min</sub>的对等方以d<sub>min</sub>的速度传输。向其它对等方以大于d<sub>min</sub>的速度传输。这样其他对等方的传输时间小于F/d<sub>min</sub>，d<sub>min</sub>的对等方时间为F/d<sub>min</sub>。  
c.  
结合a与b，如果u<sub>s</sub>/N <= d<sub>min</sub>，此时NF/u<sub>s</sub> >= F/d<sub>min</sub>，我们选择a方式来传输。
如果u<sub>s</sub>/N > d<sub>min</sub>，此时NF/u<sub>s</sub> < F/d<sub>min</sub>，选择b方式来传输。

* **P24**  
不会做。

* **P25**  
结点 N  
边 N(N-1)/2

* **P26**  
a.  
可能。因为BitTorrent有随机选择对等方发送的制度，假设时间充裕，总有机会收到文件的整个副本。  
b.  
多台计算机分别加入BitTorrent，且随时通知各个计算机自己所获得的块，使多台计算机不用索取已经获得的块。最后将获得的所有块拼接起来形成完成的副本。  

* **P27**  
对等方3询问其第一个后继，对等方4的第一个后继是什么？  
此时对等方4已经知道其第一个后继对等方5已经离开，对等方4将其第二个后继对等方8设置为第一个后继，并向对等方8发送报文询问对等方8的第一个后继。对等方4向对等方3返回对等方8作为对等方4的第一个后继。    
对等方8返回对等方10作为对等方8的第一个后继。  
对等方3收到对等方4的第一个后继是对等方8，把对等方8设为自己的第二个后继。  
对等方4收到对等方8的第一个后继四对等方10，把对等方10设为自己的第二个后继。  

* **P28**  
对等方6发送查询报文，查询键6是哪个对等方负责。返回是对等方8负责。  
对等方6把对等方8设为对等方6的直接后继。
对等方6询问对等方8的直接前驱和直接后继，返回对等方8的直接前驱是5，直接后继是10。
对等方6把对等方10设置为第二个后继，把对等方5设置为直接前驱。
对等方6通知对等方5，使其把对等方6设为直接后继。
对等方5把对等方6设为直接后继，把原来的直接后继对等方8设置为第二个后继。
对等方6通知对等方8，使其把直接前驱设置为6。

* **P29**  
不会做。

* **P30**  
如果把键与对等方的IP相关联，就一般不会产生这种错误匹配。  
如果出现这种错误匹配，则会降低查询时间。  

* **P31**  
a.  
```
python C:\Users\jz\Desktop\TCPClient.py
Traceback (most recent call last):
  File "C:\Users\jz\Desktop\TCPClient.py", line 11, in <module>
    clientSocket.connect((serverName, serverPort))
ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
```
由于服务器未开启，无法成功连接。  
b.  
```
python C:\Users\jz\Desktop\UDPClient.py
Input lowercase sentence:vjk
Traceback (most recent call last):
  File "C:\Users\jz\Desktop\UDPClient.py", line 15, in <module>
    modifiedMessage ,serverAddress = clientSocket.recvfrom(2048)
ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
```
先构造了一个数据报文并传送，但是无法收到服务器的报文。  
c.  
与上述现象相同。  

* **P32**  
没有必要修改UDPServer.py   
变化前端口号：  
UDPClient： 任意  
UDPServer： 12000  
变化后端口号：  
UDPClient： 5432  
UDPServer： 12000  

* **P33**  
可以配置。  
并行的连接数量大，可以提高网页内容的加载速度。  

* **P34**  
没有理解题目问什么。  

* **P35**  
```
Apache HTTP Server（简称Apache）是Apache软件基金会的一个开放源码的网页服务器，可以在大多数计算机操作系统中运行，由于其多平台和安全性被广泛使用，是最流行的Web服务器端软件之一。它快速、可靠并且可通过简单的API扩展，将Perl/Python等解释器编译到服务器中。
来自百度百科
```

* **P36**  
键是Torrent标识符，值是IP地址的列表。  

