# -*- coding:utf-8 -*-
# author:DragonCheng
# Data: 2022/9/14
# function: socket图像传输

import socket
import os
import sys
import struct


def sock_client_image():
    while True:
        try:
            host = "192.168.2.92"
            port = 6666
            tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpclient.connect((host, port))
        except socket.error as msg:
            print(msg)
            print(sys.exit(1))

        filepath = input('input the file: ')  # 输入当前目录下的图片名
        # struct.pack 按照给定的格式(fmt),把数据转换成字符串(字节流),并将该字符串返回.
        fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding='utf-8'),
                            os.stat(filepath).st_size)  # 将图片以128sq的格式打包
        tcpclient.send(fhead)
        fp = open(filepath, 'rb')  # 打开要传输的图片
        while True:
            data = fp.read(1024)  # 读入图片数据
            if not data:
                print('{0} send over...'.format(filepath))
                break
            print(data)
            tcpclient.send(data)  # 以二进制格式发送图片数据
        tcpclient.close()
        # break    # 注释则循环发送


if __name__ == '__main__':
    sock_client_image()
