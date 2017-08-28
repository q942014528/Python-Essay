#coding=utf-8
from SocketServer import (TCPServer as tcp,StreamRequestHandler as srh) 

from time import ctime


class myRequestHandler(srh):

    def handle(self):
        print".....connected from:",self.client_address
        self.wfile.write("[%s]"%ctime())
addr = ("",8080)
tcpser = tcp(addr,myRequestHandler)
print "wait"


tcpser.serve_forever()
#创建SocketServerTCP服务器：  
# import SocketServer  
# from SocketServer import StreamRequestHandler as SRH  
# from time import ctime  
  
# host = ''  
# port = 9999  
# addr = (host,port)  
  
# class Servers(SRH):  
#     def handle(self):  
#         print 'got connection from ',self.client_address  
#         self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))  
#         while True:  
#             data = self.request.recv(1024)  
#             if not data:   
#                 break  
#             print data  
#             print "RECV from ", self.client_address[0]  
#             self.request.send(data)  
# print 'server is running....'  
# server = SocketServer.ThreadingTCPServer(addr,Servers)  
# server.serve_forever()  