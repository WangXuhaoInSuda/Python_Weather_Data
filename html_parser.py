
from bs4 import BeautifulSoup as bs


class HtmlParser(object):
    def parse(self, html):
        final_list=[]
        soup = bs(html, 'html.parser')

        # 查找7日天气
        data = soup.find_all('ul',class_='t clearfix')
        #print(data)
        li = data[0].find_all('li')

        for i in li :
            temp_list=[]

            day = i.find('h1').string
            #print(day)
            temp_list.append(day)

            wea = i.find(class_='wea').string
            #print(wea)
            temp_list.append(wea)

            high_temperature = i.find('span').string
            #print(high_temperature)
            temp_list.append(high_temperature)

            low_temperature = i.find('i').string
            #print(low_temperature)
            temp_list.append(low_temperature)

            wind = i.find(class_='win').find('i').string
            #print(wind)
            temp_list.append(wind)
            final_list.append(temp_list)

        data = soup.find(class_='curve_livezs')
        #print(data)
        time = data.find(class_='time')
        em = time.find_all('em')
        time_list = []
        for i in em:
            time_list.append(i.string)

        time_tmp = data.find(class_='tem')
        em = time_tmp.find_all('em')
        timetmp_list = []
        for i in em:
            timetmp_list.append(i.string[0:2])
        return final_list,time_list,timetmp_list