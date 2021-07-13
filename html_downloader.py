import requests
#import dryscrape
from selenium import webdriver


class HtmlDownloader(object):
    def download(self,requrl):
        driver = webdriver.Chrome() # 调用本地的火狐浏览器，Chrom 甚至 Ie 也可以的
        driver.get(requrl)  # 请求页面，会打开一个浏览器窗口
        html_text1 = driver.page_source
        driver.quit()
        return html_text1






