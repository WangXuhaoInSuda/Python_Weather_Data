from pyecharts.charts import Page
from pyecharts import options as opts
from pyecharts.charts import Line
from collections import Counter
from pyecharts.charts import Pie
from pyecharts.components import Table
from pyecharts.globals import ThemeType


class HtmlOutputer(object):

    def outputer(self,data_list,time_list, timetmp_list):

        x = []
        high_temp = []
        low_temp = []
        weather = []
        wind = []
        for i in data_list:
            #print(i[0])
            x.append(i[0])

            #print(i[2])
            high_temp.append(i[2])
            #print(i[3][0:2])
            low_temp.append(i[3][0:2])

            weather.append(i[1])

            wind.append(i[4])



        weather_count = Counter(weather)

        line1 = (
            Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
            .add_xaxis(x)
            .add_yaxis("最高气温",high_temp,is_smooth=True)
            .add_yaxis("最低气温",low_temp,is_smooth=True)
            .set_global_opts(title_opts=opts.TitleOpts(title='哈尔滨7日气温'))
            )

        line2 = (
            Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
                .add_xaxis(time_list)
                .add_yaxis("实时气温", timetmp_list, is_smooth=True)
                .set_global_opts(title_opts=opts.TitleOpts(title='分时段预报'))
        )

        pie = Pie(init_opts=opts.InitOpts(width="600px",height="400px",theme=ThemeType.CHALK))
        pie.set_global_opts(
            title_opts={"text":"哈尔滨七天最多的天气"},
            legend_opts=opts.LegendOpts(type_='scroll',pos_top='20%',pos_left='left',orient='vertical')
        )
        catalog=[]
        percent=[]
        for i,j in weather_count.items():
            catalog.append(i)
            percent.append(j)
        data_pair=[list(d) for d in zip(catalog,percent)]
        pie.add('类别',data_pair,rosetype='radius',radius=['30%','55%'])

        table = Table('天气','')

        temp_list=[[0]*7 for i in range(2)]
        temp_list[0][0]=weather[0].encode('GB2312').decode('GBK')
        temp_list[0][1]=weather[1].encode('GB2312').decode('GBK')
        temp_list[0][2]=weather[2].encode('GB2312').decode('GBK')
        temp_list[0][3]=weather[3].encode('GB2312').decode('GBK')
        temp_list[0][4]=weather[4].encode('GB2312').decode('GBK')
        temp_list[0][5]=weather[5].encode('GB2312').decode('GBK')
        temp_list[0][6]=weather[6].encode('GB2312').decode('GBK')
        temp_list[1][0] = wind[0].encode('GB2312').decode('GBK')
        temp_list[1][1] = wind[1].encode('GB2312').decode('GBK')
        temp_list[1][2] = wind[2].encode('GB2312').decode('GBK')
        temp_list[1][3] = wind[3].encode('GB2312').decode('GBK')
        temp_list[1][4] = wind[4].encode('GB2312').decode('GBK')
        temp_list[1][5] = wind[5].encode('GB2312').decode('GBK')
        temp_list[1][6] = wind[6].encode('GB2312').decode('GBK')
        table.add(headers=x,rows=temp_list,attributes=None)
        table.set_global_opts(title_opts={"text":"分时天气","subtext":""})

        page=Page(layout=Page.DraggablePageLayout,page_title="气温数据展示大屏")
        line1.chart_id="line1"
        line2.chart_id='line2'
        pie.chart_id='pie'
        table.chart_id='table'
        page.add(line1,pie,table,line2)
        page.render("./气温数据展示大屏.html")
        page.save_resize_html("./气温数据展示大屏.html",cfg_file="./chart_config.json",dest="final.html")
