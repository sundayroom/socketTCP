import socket

client=socket.socket()
client.connect(('127.0.0.1',6000))

while True:
    msg=input("<<请输入").strip()
    if len(msg)==0:continue
    ss=client.send(msg.encode('utf-8'))
    print("send:",ss)
    data = client.recv(1024)
    print(data.decode('utf-8'))
client.close

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Colin Yao
#客户端
# import socket
# client = socket.socket() #定义协议类型,相当于生命socket类型,同时生成socket连接对象
# client.connect(('192.168.84.130',9999))
# while True:
#     msg = input(">>>").strip()
#     if len(msg) ==0:continue
#     client.send(msg.encode("utf-8"))
#     data = client.recv(1024)#这里是字节1k
#     print("recv:>",data.decode())
# client.close()