# -*- coding:utf-8 -*-
# author:DragonCheng
# Data: 2022/9/14
# function: sockets communicate server

import socket
import time

# 1.创建通信用的socket对象
server = socket.socket()
# 2.绑定一个IP和端口
server.bind(('192.168.2.58',8090))                  # 一个地址族中的特定地址赋给socket

# 3.调用 listen() 方法开始监听端口，
server.listen(4)                                    # 监听其绑定ip和端口，如果客户端这时调用connect()发出连接请求，服务器端就会接收到这个请求。

# 4、如果有客户端进行连接、则接受客户端的连接（调用accept阻塞等待客户端连接）
serObj,address = server.accept()                   # 返回客户端socket通信对象和客户端的ip
print("客户端连接成功 ...")
# 当有客户端访问时，实现两边的交流，如果有一方退出，整个程序退出。
# 服务器程序通过一个永久循环来接受来自客户端的连接
# 这里虽然给出最大连接数为4，但单线程程序也只会响应一个连接

while True:
    # 建立连接后，服务端等待客户端发送的数据，实现通信
    # 5、客户端与服务端进行通信
    re_data = serObj.recv(1024).decode('utf-8')
    print("服务器接收到客户端的数据:",time.strftime("%Y-%m-%d %X",time.localtime()),re_data)
    # send_data = input('server>>')
    # 6、服务端给客户端回消息
    # serObj.send(send_data.encode('utf-8'))
    serObj.send(b'server>>')
    if re_data == 'quit':
        break
    time.sleep(1)
# 7、关闭socket对象
serObj.close()  # 关闭客户端对象
server.close()  # 关闭服务端对象
