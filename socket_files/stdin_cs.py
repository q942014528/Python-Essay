from sys import *
import select



epoll = select.epoll()
epoll.register(stdin,select.EPOLLOUT)

events = epoll.poll()
for e,i in events:
    if e==stdin.fileno():
        print "*********"
        print stdin.readline().strip("\n")
    else:
        print "errno"