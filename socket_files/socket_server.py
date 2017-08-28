#coding=utf-8
from socket import *
from time import ctime
import select 
import chardet
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",8081))
s.listen(5)
epoll = select.epoll()
epoll.register(s.fileno(),select.EPOLLIN)
conn = {}
addrs ={}
while True:
    events = epoll.poll()
    
    for fileno,event in events:
        if fileno == s.fileno():
            tcpcli ,addr = s.accept()
            tcpcli.setblocking(0)
            tcpcli.send("OK")
            epoll.register(tcpcli.fileno(),select.EPOLLIN)
            conn[tcpcli.fileno()]=tcpcli
            addrs[tcpcli.fileno()] = addr

        elif select.EPOLLIN & event:
            data = ""
            
            try:
                data = conn[fileno].recv(1024)
                # conn[fileno].setblocking(0)
                print chardet.detect(data)
                addr_tmp = addrs[fileno]
            except KeyError as e:
                print e
            if not data:
                
                epoll.unregister(fileno)
                conn[fileno].close()
                break
            for i in conn.values():
                
                datas = "地址:%s,%s"%(addr_tmp[0],addr_tmp[1])+"\n"+"data:"+data
                i.send(datas)
            
            print "地址:%s,%s"%(addr_tmp[0],addr_tmp[1])
s.close()
