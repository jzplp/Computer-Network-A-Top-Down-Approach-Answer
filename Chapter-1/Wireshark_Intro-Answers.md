<ul>

<li><b>
1. 列出上述步骤7中出现在未过滤的分组列表窗口的协议列中的3种不同的协议。
</b></li>
<p>
答案：<br/>
HTTP协议，TCP协议，DNS协议
</p>

<li><b>
2. 从HTTP GET消息发送到HTTP OK回复需要多长时间？
</b></li>
<p>
答案：<br/>
用了0.250858s
</p>

<li><b>
3. gaia.cs.umass.edu(也称为www.net.cs.umass.edu)的Internet地址是什么？您的计算机的Internet地址是什么？
</b></li>
<p>
答案：<br/>
gaia.cs.umass.edu的Internet地址是128.119.245.12<br/>
我的计算机的Internet地址是 49.52.10.72
</p>

<li><b>
4. 打印问题2提到的两个HTTP消息(GET和OK)。
</b></li>
<p>
答案：<br/>
GET消息：<br/>
  
No.     Time               Source                Destination           Protocol Length Info
    310 14:16:35.846326    49.52.10.72           128.119.245.12        HTTP     359    GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1 

Frame 310: 359 bytes on wire (2872 bits), 359 bytes captured (2872 bits) on interface 0
Ethernet II, Src: Dell_26:61:cc (50:9a:4c:26:61:cc), Dst: Cisco_f1:9d:c0 (58:97:bd:f1:9d:c0)
Internet Protocol Version 4, Src: 49.52.10.72, Dst: 128.119.245.12
Transmission Control Protocol, Src Port: 65117, Dst Port: 80, Seq: 1, Ack: 1, Len: 305
Hypertext Transfer Protocol
    GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\n
    Accept: text/html, application/xhtml+xml, image/jxr, */*\r\n
    Accept-Language: zh-CN\r\n
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko\r\n
    Accept-Encoding: gzip, deflate\r\n
    Host: gaia.cs.umass.edu\r\n
    Connection: Keep-Alive\r\n
    \r\n
    [Full request URI: http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html]
    [HTTP request 1/1]
    [Response in frame: 316]
    
OK消息：<br/>

No.     Time               Source                Destination           Protocol Length Info
    316 14:16:36.097184    128.119.245.12        49.52.10.72           HTTP     492    HTTP/1.1 200 OK  (text/html)

Frame 316: 492 bytes on wire (3936 bits), 492 bytes captured (3936 bits) on interface 0
Ethernet II, Src: Cisco_f1:9d:c0 (58:97:bd:f1:9d:c0), Dst: Dell_26:61:cc (50:9a:4c:26:61:cc)
Internet Protocol Version 4, Src: 128.119.245.12, Dst: 49.52.10.72
Transmission Control Protocol, Src Port: 80, Dst Port: 65117, Seq: 1, Ack: 306, Len: 438
Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
    Date: Mon, 22 Oct 2018 06:16:35 GMT\r\n
    Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/5.4.16 mod_perl/2.0.10 Perl/v5.16.3\r\n
    Last-Modified: Mon, 22 Oct 2018 05:59:01 GMT\r\n
    ETag: "51-578caf3246024"\r\n
    Accept-Ranges: bytes\r\n
    Content-Length: 81\r\n
    Keep-Alive: timeout=5, max=100\r\n
    Connection: Keep-Alive\r\n
    Content-Type: text/html; charset=UTF-8\r\n
    \r\n
    [HTTP response 1/1]
    [Time since request: 0.250858000 seconds]
    [Request in frame: 310]
    File Data: 81 bytes
Line-based text data: text/html (3 lines)
    <html>\n
    Congratulations!  You've downloaded the first Wireshark lab file!\n
    </html>\n


</p>

</ul>
