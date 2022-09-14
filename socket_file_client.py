# -*- coding:utf-8 -*-
# author:DragonCheng
# Data: 2022/9/14
# function: 接收文件(不包含PDF文件)

import socket

host = "192.168.2.92"
port = 6666
tcpclient = socket.socket()

try:
    tcpclient.connect((host, port))
    print('服务器已连接')
except:
    print('服务器连接失败，请修改后重新运行!!')
    exit(0)

while True:
    print("-" * 5 + "开始发送" + "-" * 5)
    filename = "rose.log"
    print(f"发送的文件为：{filename}")
    with open(filename, "r", encoding="utf-8") as f:
        rdata = f.read()
    tcpclient.send("qq.txt".encode("utf-8"))
    if tcpclient.recv(1024).decode("utf-8") == "ok":
        while True:
            tcpclient.send(rdata.encode('utf-8'))
            break
    print("-" * 5 + "发送完成" + "-" * 5)
    break

tcpclient.close()