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
        pass
    def create_epoll(self):
        pass
    def connection(self):
        pass
    def Create_chatroom(self,tcp_client):
        pass
    def Delete_chatroom(self):
        pass
    def soc_close(self,conn): 
        pass
    