from socket import *

s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(5)

c, addr = s.accept()
print('connect from', addr)

data = c.recv(1024)
print(data.decode())

# 发送HTTP相应给浏览器
response = """HTTP/1.1 200 OK
Content-Type:text/html

Hello world
"""
#双引号写法：

c.send(response.encode())

c.close()
