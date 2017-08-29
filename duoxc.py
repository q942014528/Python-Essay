#coding=utf-8
import requests
import urllib2
import sys
from lxml import etree
import threading
from Queue import Queue
import time
import datetime
class Spider(threading.Thread):
    def __init__(self,event):
        super(Spider,self).__init__()
        self.headers = { "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.url = 'http://www.biquge.com.tw/'
        self.threadEvent = event

    def run(self):
        global starttime
        self.nums = 0
        self.req = requests.get(self.url+'0_14/',headers = self.headers)
        # self.req.encoding='gbk'
        # texts = self.req.text.encode('utf-8')


        html = etree.HTML(self.req.text)
        SonUrl = html.xpath('*//div/dl/dd/a/@href')
        for i in SonUrl:
            if url.qsize() == 10:
                
                self.threadEvent.wait()

            url.put(i)    
            self.nums+=1
            
              

class NovelSpider(threading.Thread):
    def __init__(self,event):
        super(NovelSpider,self).__init__()
        self.headers = { "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.url = 'http://www.biquge.com.tw/'
        self.threadEvent = event


    def run(self):
        global starttime
        print starttime
        a = time.time()
        b = 0
        while True:
            if url.empty():
                self.threadEvent.set()
                b = time.time()

            if url.qsize() >0:
                
                self.Novelurls = url.get()
                self.urls = self.url+self.Novelurls
                self.request = requests.get(self.urls,headers = self.headers)
                self.request.encoding='gbk'
            
                Novel = etree.HTML(self.request.text)
                title = Novel.xpath('*//div[@class="bookname"]/h1')
                txt = Novel.xpath('*//div[@id="content"]/text()')
                # for i in txt:
                title = title[0].text
                a = time.time()
                for i in txt:
                    with open('txt/%s.txt'%title,'a') as file:
                        file.write(i.encode('utf-8'))
            
            if b - a >10:
                print '---------'
                break
        
        endtime = datetime.datetime.now()
        longtime = (endtime-starttime).seconds
        print '程序运行时间:%d'%longtime







        # self.urls = self.url+i
        # print self.urls
        # self.request = requests.get(self.urls,headers = self.headers)
        # self.request.encoding='gbk'
        
        # Novel = etree.HTML(self.request.text)
        # title = Novel.xpath('*//div[@class="bookname"]/h1')
        # txt = Novel.xpath('*//div[@id="content"]/text()')
        # # for i in txt:
        # title = title[0].text
        # for i in txt:
        #     with open('txt/%s.txt'%title,'a') as file:
        #         file.write(i.encode('utf-8'))
                

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    url = Queue(50)
    event = threading.Event()
    for i in range(5):
        t = Spider(event)
        t.start()
        n = NovelSpider(event)
        n.start()