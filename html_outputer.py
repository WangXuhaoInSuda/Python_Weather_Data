from pyecharts.charts import Page
from pyecharts import options as opts
from pyecharts.charts import Line
from collections import Counter
from pyecharts.charts import Pie
class HtmlOutputer(object):

    def outputer(self,data_list):

        x = []
        high_temp = []
        low_temp = []
        weather = []
        for i in data_list:
            #print(i[0])
            x.append(i[0])

            #print(i[2])
            high_temp.append(i[2])
            #print(i[3][0:2])
            low_temp.append(i[3][0:2])

            weather.append(i[1])

        weather_count = Counter(weather)

        line = (
            Line()
            .add_xaxis(x)
            .add_yaxis("最高气温",high_temp,is_smooth=True)
            .add_yaxis("最低气温",low_temp,is_smooth=True)
            .set_global_opts(title_opts=opts.TitleOpts(title='哈尔滨7日气温'))
            )

        pie = Pie(init_opts=opts.InitOpts(width="600px",height="400px"))
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

        page=Page(layout=Page.DraggablePageLayout,page_title="气温数据展示大屏")
        page.add(line,pie)
        page.render("./气温数据展示大屏.html")
