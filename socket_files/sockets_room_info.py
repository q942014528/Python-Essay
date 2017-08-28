#coding=utf-8
from socket import *
from time import ctime
import select 
import chardet
import sys
import select
reload(sys)
sys.setdefaultencoding('UTF-8')
class Room_handler(object):
    def __init__(self,soc):
        self.soc=soc
        self.fileno = ""
        self.tcpcli = ''
        self.addr = ''
        self.epoll = ''
        self.conn = {}
        self.addrs = {}
        self.room_list =[]
    def room_info(self,fileno,epoll,exit=False):
        self.epoll = epoll

        if exit:
            return self.conn
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
                return 0
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