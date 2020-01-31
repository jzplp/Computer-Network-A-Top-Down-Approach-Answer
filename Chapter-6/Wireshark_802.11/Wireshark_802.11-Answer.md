### Wireshark_802.11  

### 2.Beacon Frames 信标帧

1. 30 Munroe St 和 linksys_SES_24086  

2. 30 Munroe St ： 0.1024 Seconds  
linksys_SES_24086 ： 并未找到  

3. 00:16:b6:f7:1d:51  
源地址是发送无线站点本身的地址，目的地址是接收无线站点的地址，基本服务集地址是指的基本服务集基础设施的地址，也就是AP的地址。  

4. ff:ff:ff:ff:ff:ff，表示广播地址  

5. 00:16:b6:f7:1d:51  

6. 
```
Tag: Supported Rates 1(B), 2(B), 5.5(B), 11(B), [Mbit/sec]
    Tag Number: Supported Rates (1)
    Tag length: 4
    Supported Rates: 1(B) (0x82)
    Supported Rates: 2(B) (0x84)
    Supported Rates: 5.5(B) (0x8b)
    Supported Rates: 11(B) (0x96)
Tag: Extended Supported Rates 6(B), 9, 12(B), 18, 24(B), 36, 48, 54, [Mbit/sec]
    Tag Number: Extended Supported Rates (50)
    Tag length: 8
    Extended Supported Rates: 6(B) (0x8c)
    Extended Supported Rates: 9 (0x12)
    Extended Supported Rates: 12(B) (0x98)
    Extended Supported Rates: 18 (0x24)
    Extended Supported Rates: 24(B) (0xb0)
    Extended Supported Rates: 36 (0x48)
    Extended Supported Rates: 48 (0x60)
    Extended Supported Rates: 54 (0x6c)
```

### 3.Data Transfer 数据传输  

7.  
接收地址： 00:16:b6:f7:1d:51  
发送地址： 00:13:02:d1:b6:4f  
目的地址： 00:16:b6:f4:eb:a8  
无线主机的MAC地址： 00:13:02:d1:b6:4f  
接入点MAC地址： 00:16:b6:f7:1d:51  
第一跳路由器的MAC地址： 00:16:b6:f4:eb:a8  
发送此TCP报文的无线主机IP是：192.168.1.109  
目的地IP地址是：128.119.245.12  
这个目的地与任何当前MAC地址的设备都不对应。  

8. 
接收地址： 91:2a:b0:49:b6:4f  
发送地址： 00:16:b6:f4:eb:a8  
目的地址： 91:2a:b0:49:b6:4f  
无线主机的MAC地址：91:2a:b0:49:b6:4f  
接入点MAC地址： 00:16:b6:f7:1d:51  
第一跳路由器的MAC地址：00:16:b6:f4:eb:a8  
帧中的发送方MAC地址与发送此TCP报文的设备的IP地址并不对应  


后面略。
