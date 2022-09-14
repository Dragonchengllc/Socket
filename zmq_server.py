# -*- coding:utf-8 -*-
# author:DragonCheng
# Data: 2022/9/14
# function: zmq test server


import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)  # 设置socket的类型，zmq.REP答复
socket.bind("tcp://*:15000")    # 绑定服务端的IP和端口

while True:                     # 循环接收客户端发来的消息
    message = socket.recv()       # 接收客户端发送来的消息，注：是byte类型
    print("zmq send data is:",time.strftime("%Y-%m-%d %X",time.localtime()),message)
    socket.send_string("zmq server received success!")  # 再发回客户端消息