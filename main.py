import sys
import os

import html_downloader, html_outputer, html_parser

class SpiderMain(object):

    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        #self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        print(f"craw:{root_url}")
        html = self.downloader.download(root_url)

        with open('html1.txt', 'w+',encoding='utf-8') as f:
            f.write(html)

        print('数据抓取完毕！')
        (data_list,time_list,timetmp_list) = self.parser.parse(html)
        self.outputer.outputer(data_list,time_list,timetmp_list)


if __name__ == "__main__":
    root_url ="http://www.weather.com.cn/weather/101050101.shtml"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    print('Done!')

