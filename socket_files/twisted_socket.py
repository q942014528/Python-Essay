#coding=utf-8

from twisted.internet import protocol,reactor

from time import ctime

class Tss(protocol.Protocol):
    def connectionMade(self): 
        clnt = self.transport.getPeer().host
        print "conn from:",clnt
    def dataReceived(self,data):
        print data
        self.transport.write("[%s],%s"%(ctime(),data))


if __name__ == "__main__":
    port = 8081
    factory = protocol.Factory()
    factory.protocol = Tss
    print "wait"
    reactor.listenTCP(port,factory)
    reactor.run()
