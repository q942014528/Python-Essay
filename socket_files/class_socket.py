#coding=utf-8
from socket import *
from time import ctime
import select 
import chardet
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
class full_duplex(object):
    def __init__(self,ip="",port=8080,listen=5):
        self.conn = {}
        self.addrs ={}
        self.ip = ip
        self.port = port
        self.listen = listen
        self.soc=""
        self.epoll = ''
        
    def create_connection(self):
        self.soc = socket(AF_INET,SOCK_STREAM)
        self.soc.bind((self.ip,self.port))
        self.soc.listen(self.listen)
    def create_epoll(self):
        self.epoll=select.epoll()
        self.epoll.register(self.soc.fileno(),select.EPOLLIN)
        self.epoll.register(sys.stdin.fileno(),select.EPOLLIN)
    def connection(self):
        while True:
            events = self.epoll.poll()
            if events[0][0] == sys.stdin.fileno():
                e = sys.stdin.readline().strip("\n")
                if e == "exit" or e == "quit":
                    print e
                    break
                else:
                    continue
            for fileno,event in events:
                if fileno == self.soc.fileno():
                    tcpcli ,addr = self.soc.accept()
                    tcpcli.setblocking(0)
                    tcpcli.send("OK")
                    self.epoll.register(tcpcli.fileno(),select.EPOLLIN)
                    self.conn[tcpcli.fileno()]=[tcpcli]
                    self.addrs[tcpcli.fileno()] = addr
                    print "%s:%s连接成功"%(addr[0],addr[1])
                elif select.EPOLLIN & event:
                    data = ""
                    try:
                        data = self.conn[fileno][0].recv(1024)
                        # conn[fileno].setblocking(0)
                        addr_tmp = self.addrs[fileno]
                        # 编码格式处理
                        # tmp = chardet.detect(data)
                        # print tmp

                        # if tmp.['encoding']=="TIS-620":
                            
                        #     self.conn[tcpcli.fileno()].append("gbk")
                        #     print "---------------"
                        #     print self.conn
                        # else:
                        #     print"******************"
                        #     self.conn[tcpcli.fileno()].append("utf-8")
                        #     print self.conn
                    except KeyError as e:
                        print e

                    if not data:
                        
                        self.epoll.unregister(fileno)
                        self.conn[fileno][0].close()
                        
                        self.conn.pop(fileno)
                       
                        print "%s%s已退出"%(self.addrs[fileno][0],self.addrs[fileno][1])
                        break
                    for i in self.conn.values():
                        # if self.conn[i[0].fileno()][1] == "gbk" and chardet.detect(data).values()[1] == "utf-8":
                        #     data = data.decode("utf-8").encode("gb2312")
                        # elif self.conn[i[0].fileno()][1] == "utf-8" and chardet.detect(data).values()[1] == "TIS-620":
                        #     data = data.decode("gb2312").encode("utf-8")
                        datas = "地址:%s,%s"%(addr_tmp[0],addr_tmp[1])+"\n"+"data:"+data  
                        i[0].send(datas)
                    print "地址:%s,%s"%(addr_tmp[0],addr_tmp[1])

        self.soc_close(self.conn)
    def soc_close(self,conn): 
        for i in self.conn.values():
            self.epoll.unregister(i[0].fileno())
            i[0].close()
            
        self.epoll.unregister(self.soc.fileno())
        self.soc.close()
        print"服务器退出"

if __name__ == "__main__":
    server = full_duplex()
    server.create_connection()
    server.create_epoll()
    server.connection()
    