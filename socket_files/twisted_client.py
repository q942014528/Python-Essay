#coding=utf-8
from twisted.internet import protocol,reactor

class tscpro(protocol.Protocol):
    def send(self):
        data = raw_input("> ")
        if data:
            print data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.send()
    
    def dataReceived(self,data):
        self.send()
    
class tscfac(protocol.ClientFactory):
    protocol = tscpro
    clientConnectionLost = clientConnectionFailed = \
        lambda self,connector,reason:reactor.stop()
    
if __name__ == "__main__":
    port = 8081
    host = ''
    reactor.connectTCP(host,port,tscfac())
    reactor.run()