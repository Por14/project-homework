# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts.charts import Pie
from pyecharts import options as opts

fruits = {'理工': 35.0, '综合': 36.0, '语言': 5.0, '财经': 15.0, '农业': 1.0,
          '医药': 3.0, '师范': 5.0}
s_fruits = pd.Series(fruits)
print(s_fruits)

# 玫瑰图
"""pie = Pie(init_opts=opts.InitOpts(width='800px', height='600px', bg_color='white'))
pie.add(
    '', [list(z) for z in zip([fruit for fruit in s_fruits.index], s_fruits)],
    radius=['10%', '70%'], center=['50%', '50%'], rosetype="radius"
).set_series_opts(
    label_opts=opts.LabelOpts(formatter="{b}: {c}")
).set_global_opts(
    title_opts=opts.TitleOpts(title='百强学校类型对比)', pos_left='300', pos_top='20',
        title_textstyle_opts=opts.TextStyleOpts(color='black', font_size=16)),
    legend_opts=opts.LegendOpts(is_show=False)
).render('fruits_calorie3.html')"""

# 玫瑰图美化
s_fruits = s_fruits.sort_values()
pie = Pie(init_opts=opts.InitOpts(width='800px', height='600px', bg_color='white'))
pie.add(
    '', [list(z) for z in zip([fruit for fruit in s_fruits.index], s_fruits)],
    radius=['10%', '70%'], center=['50%', '50%'], rosetype="radius"
).set_series_opts(
    label_opts=opts.LabelOpts(formatter="{b}: {c}"),
).set_global_opts(
    title_opts=opts.TitleOpts(title='百强学校类型对比', pos_left='300', pos_top='20',
                              title_textstyle_opts=opts.TextStyleOpts(color='black', font_size=16)),
    legend_opts=opts.LegendOpts(is_show=False)
).set_colors(
    ['rgb({r},0,{b})'.format(r=255 - 20 * (len(s_fruits) - x + 1), b=255 - 15 * x) for x in range(len(s_fruits))]
).render('玫瑰图.html')
# plt.savefig('tu4.png')
