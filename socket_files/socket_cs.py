#coding=utf-8
from socket import *
import select 
from sys import *
# addr = ("192.168.133.1",8080)
addr = ("127.0.0.1",4444)
tcp_cli = socket(AF_INET,SOCK_STREAM)
tcp_cli.connect(addr)
epoll = select.epoll()

epoll.register(stdin,select.EPOLLIN)
epoll.register(tcp_cli.fileno(),select.EPOLLIN)
data = "0"
while True:
    events = epoll.poll()
    recvs = ""
    for fileno,event in events:
        
        if fileno == stdin.fileno():
            
            data = stdin.readline().strip("\n")
            if not data:
                print"退出,拜拜"
                epoll.unregister(tcp_cli.fileno())
                epoll.unregister(stdin)
                
                break
            tcp_cli.send(data)

        elif fileno == tcp_cli.fileno():
            recvs = tcp_cli.recv(1024)
            if recvs ==None:
                break
            print "recv:"+recvs
    if not recvs:
        print "服务器退出"
        break
    elif not data:
        break
print"exit"
tcp_cli.close()