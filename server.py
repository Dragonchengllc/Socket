# -*- coding:utf-8 -*-
# author:DragonCheng
# Data: 2022/9/14
# function: camera获取图像实时传输

import cv2
import zmq
import base64
import numpy as np


def main():
    context = zmq.Context()
    footage_socket = context.socket(zmq.PAIR)
    footage_socket.bind('tcp://*:15000')
    cv2.namedWindow('Stream', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    while True:
        print("监听中...")
        frame = footage_socket.recv()  # 接收TCP传输过来的一帧视频图像数据
        print("监听中1...")
        img = base64.b64decode(frame)  # 把数据进行base64解码后储存到内存img变量中
        npimg = np.frombuffer(img, dtype=np.uint8)  # 把这段缓存解码成一维数组
        source = cv2.imdecode(npimg, 1)  # 将一维数组解码为图像source
        cv2.imshow("Stream", source)  # 把图像显示在窗口中
        cv2.waitKey(1000)  # 延时等待，防止出现窗口无响应


if __name__ == '__main__':
    main()
