#coding=utf-8
from socket import *
import select 
from sys import *
# addr = ("192.168.133.1",8080)
addr = ("",8082)
tcp_cli = socket(AF_INET,SOCK_STREAM)
tcp_cli2 = socket(AF_INET,SOCK_STREAM)
tcp_cli.bind(addr)
tcp_cli.listen(5)
tcp_cli2.bind(("",8083))
tcp_cli2.listen(5)

s,a = tcp_cli.accept()
s2,a2 = tcp_cli2.accept()
data = s.recv(1024)
data2 = s2.recv(1024)
print "data:",data
print "data2:",data2
s.close()