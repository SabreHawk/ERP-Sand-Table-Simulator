
# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# 获取本地主机名
host = '45.77.112.171'
# 设置端口好
port = 1830
# 连接服务，指定主机和端口
s.connect((host, port))
# 接收小于 1024 字节的数据
s.send('sys_login "root" "root"'.encode('utf-8'))
msg = s.recv(1024).decode('utf-8')
print(msg)
s.close()