# -*- coding:utf-8 -*-
# author:DragonCheng
# Data: 2022/9/14
# function: socket通信

import socket
import time

# 1.创建socket通信对象
client = socket.socket()
# 2.连接服务器
client.connect(('192.168.2.58',8090))

while True:
    # send_data = input("client send data >>>")
    # client.send(send_data.encode('utf-8'))
    # 3.给socket服务器发送信息
    client.send(b'client send data >>>')
    # 4.从服务器接收数据
    re_data = client.recv(1024).decode('utf-8')
    if re_data == 'quit':
        break
    print("客户端接收到服务器的数据为:",time.strftime("%Y-%m-%d %X",time.localtime()),re_data)
    time.sleep(1)

# 5.关闭socket对象
client.close()
