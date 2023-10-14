# 保存为 client.py

import socket

# 创建UDP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 目标服务器的IP地址和端口
server_address = ('192.168.31.18', 12345)

while True:
    message = input('请输入要发送的消息: ')
    
    # 发送消息
    client_socket.sendto(message.encode(), server_address)
# 保存为 server.py