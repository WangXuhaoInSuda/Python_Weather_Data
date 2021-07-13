import sys
import requests


class HtmlDownloader(object):
    def download(self, requrl):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Cookie':'Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1626135942; userNewsPort0=1; f_city=%E5%93%88%E5%B0%94%E6%BB%A8%7C101050101%7C; zs=101050101%7C%7C%7Cyd-uv; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1626145425',
        }
        try:
            req = requests.get(requrl, headers=headers)
            req.raise_for_status()
            req.encoding = req.apparent_encoding

            req2= requests.get("http://d1.weather.com.cn/travel_rank/3A10105.html?_=1626149572473",headers=headers)
            req2.raise_for_status()
            req2.encoding = req2.apparent_encoding

        except Exception as e:
            print(e)
        else:
            return req.text,req2.text
