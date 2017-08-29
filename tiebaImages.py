#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
from lxml import etree

class tiebaSpider():
    def __init__(self):
        self.tiebaName = raw_input("请需要访问的贴吧：")
        self.beginPage = int(raw_input("请输入起始页："))
        self.endPage = int(raw_input("请输入终止页："))
        self.url = 'http://tieba.baidu.com/f'
        self.headers = { "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.num = 1

    def spiderWork(self):
        for page in range(self.beginPage, self.endPage + 1):
            pn = (page - 1) * 50 # page number
            word = {'pn' : pn, 'kw': self.tiebaName}
            word = urllib.urlencode(word) #转换成url编码格式（字符串）
            myUrl = self.url + "?" + word
            links = self.loadPage(myUrl)

            for link in links:
                link = "http://tieba.baidu.com" + link
                # print link
                self.loadImages(link)

    def loadPage(self, url):
        # 按照参数构造一个http请求信息，返回一个构造好的请求对象
        req = urllib2.Request(url, headers = self.headers)

        # 按照构造内容发送这个请求，返回一个 类文件 对象
        html = urllib2.urlopen(req).read()

        selector = etree.HTML(html)
        # print type(selector)

        #抓取当前页面的所有帖子的url
        links = selector.xpath('*//div[@class="t_con cleafix"]/div/div/div/a/@href')
        print links
        # 将里面的内容返回给调用函数
        return links


    # 获取图片
    def loadImages(self, link):
        html = urllib2.urlopen(link).read()

        selector = etree.HTML(html)

        imagesLinks = selector.xpath('*//img[@class="BDE_Image"]/@src')

        for imagesLink in imagesLinks:
            # print imagesLink
            self.writeImages(imagesLink)

    # 保存页面内容
    def writeImages(self, imagesLink):
        print "正在存储文件 ...", self.num
        # 1. 打开文件，返回一个文件对象
        file = open('images/' + str(self.num)  + '.gif', "wb")
        # 2. 获取图片里的内容
        images = urllib2.urlopen(imagesLink).read()
        # 3. 调用文件对象write() 方法，将page_html的内容写入到文件里
        file.write(images)
        # 4. 最后关闭文件
        file.close()

        self.num += 1

if __name__ == '__main__':
    spider = tiebaSpider()
    spider.spiderWork()


#=================================================================


