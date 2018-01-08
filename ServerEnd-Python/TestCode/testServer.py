import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = '127.0.0.1'
port = 1831
serversocket.bind((host_ip, port))
# 设置最大连接数，超过后排队
serversocket.listen(5)
msg = "received your request Sabrehawk"
while True:
    # 建立客户端连接
    (clientsocket,addr) = serversocket.accept()      
    clientsocket.send(msg.encode('utf-8'))
    __request_msg = clientsocket.recv(1024).decode('utf-8').split()
    print(__request_msg)
    clientsocket.close()

print("Server End")

