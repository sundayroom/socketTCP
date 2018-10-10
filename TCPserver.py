import socketserver

class MyTCPserver(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data=self.request.recv(1024).strip()
                print("您已经接收数据:",self.data)
                self.request.sendall(self.data.upper())
                print("您已经发送数据:")
            except ConnectionResetError as e:
                break


host,port="127.0.0.1",6000
serverTCP = socketserver.TCPServer(("127.0.0.1", 6000), MyTCPserver)
print("***连接成功***")
#server=socketserver.ThreadingTCPServer((host,port),MyTCPserver)
serverTCP.serve_forever()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Colin Yao

# import socketserver
#
# class MyTCPHandler(socketserver.BaseRequestHandler):
#
#     def handle(self):  #所有请求的交互都是在handle里执行的,
#         while True:
#             try:
#                 self.data = self.request.recv(1024).strip()#每一个请求都会实例化MyTCPHandler(socketserver.BaseRequestHandler):
#                 print("{} wrote:".format(self.client_address[0]))
#                 print(self.data)
#                 self.request.sendall(self.data.upper())#sendall是重复调用send.
#             except ConnectionResetError as e:
#                 print("err ",e)
#                 break
#
# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999 #windows
#     #HOST, PORT = "0.0.0.0", 9999 #Linux
#     server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)   #线程
#     server.serve_forever()