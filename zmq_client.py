# -*- coding:utf-8 -*-
# author:DragonCheng
# Data: 2022/9/14
# function: zmq通信传输

import zmq
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)          # 设置socket类型，请求端
socket.connect("tcp://localhost:15000")   # 连接服务端的IP和端口

while True:
    data = input("input your request:")
    if data == "q":
        sys.exit()
    socket.send_string(data)           # 向服务端发送消息
    message = socket.recv()            # 接收服务端返回的消息，注：是byte类型
    print(time.strftime("%Y-%m-%d %X",time.localtime()), message)
