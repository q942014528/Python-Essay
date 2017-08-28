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
        # 房间数量
        self.room_num = 0
        # 房间名称
        self.room_list = []
        # 房间人数
        self.room_dict = {}
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
                    self.epoll.register(tcpcli.fileno(),select.EPOLLIN)
                    self.conn[tcpcli.fileno()]=[tcpcli,0]
                    self.addrs[tcpcli.fileno()] = addr
                    print "%s:%s连接成功"%(addr[0],addr[1])
                    room =""
                    if self.room_list:
                        tcpcli.send("请选择聊天室:\n *号创建聊天室\n")
                        for i in self.room_list:
                            if i>0:
                                room += "聊天室:%d号\n人数:%d"%(i,self.room_dict[i])
                                
                        tcpcli.send(room)
                    else:
                        tcpcli.send("当前无聊天室\n请创建聊天室，按*号创建聊天室")
                elif select.EPOLLIN & event:
                    data = ""
                    tcp_client = self.conn[fileno]
                    try:
                        data = tcp_client[0].recv(1024)
                        # conn[fileno].setblocking(0)
                        addr_tmp = self.addrs[fileno]    
                    except KeyError as e:
                        print e
                    if not data:
                        
                        self.epoll.unregister(fileno)
                        tcp_client[0].close()
                        
                        self.conn.pop(fileno)
                        
                        print "%s%s已退出"%(self.addrs[fileno][0],self.addrs[fileno][1])
                        break
                    if tcp_client[1]==0:
                        
                        if data=="*":
                            self.Create_chatroom(tcp_client)
                            tcp_client[0].send("创建房间成功\n进入%d号聊天室"%self.room_num)
                            
                        elif int(data) in self.room_list:
                            data = int(data)
                            tcp_client[1] = data
                            
                            self.room_dict[data] = self.room_dict[data]+1
                            tcp_client[0].send("进入%d号聊天室\n人数%d"%(data,self.room_dict[data]))
                            for i in self.conn.values():
                                if i[1] == tcp_client[1]:
                                    i[0].send("%d 进入聊天室"%addr_tmp[0])

                        else:
                            print tcp_client
                            tcp_client[0].send("当前无这个聊天室\n请创建聊天室，按*号创建聊天室-----")
                    else:
                        for i in self.conn.values():
                            if i[1] == tcp_client[1]:
                                i[0].send("%s,%s [%s]:%s"%(addr_tmp[0],addr_tmp[1],ctime(),str(data)))

                    print "地址:%s,%s"%(addr_tmp[0],addr_tmp[1])

        self.soc_close(self.conn)

    def Create_chatroom(self,tcp_client):
        self.room_num+=1
        tcp_client[1] = self.room_num
        self.room_list.append(self.room_num)
        # 房间号与人数
        self.room_dict[self.room_num] = 1
    def Delete_chatroom(self):
        pass

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
    