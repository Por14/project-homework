from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data1 = [
    ("上海市",2),
    ("云南省",2),
    ("北京市",1),
    ("吉林省",7),
    ("四川省",3),
    ("宁夏回族自治区",1),
    ("安徽省",8),
    ("山东省",10),
    ("山西省",1),
    ("广东省",10),
    ("广西壮族自治区",1),
    ("江苏省",2),
    ("江西省",2),
    ("河北省",4),
    ("河南省",12),
    ("浙江省",2),
    ("海南省",1),
    ("湖北省",7),
    ("湖南省",1),
    ("福建省",4),
    ("辽宁省",5),
    ("重庆市",6),
    ("陕西省",5),
    ("黑龙江省",1)
]
#添加数据
map.add("2022前100地区分布图",data1,"china")
#设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":0,"max":3,"label":"1-3","color":"#CCFFFF"},
            {"min": 3, "max": 6, "label": "3-6", "color": "#FFDEAD"},
            {"min": 6,"max": 9, "label": "6-9", "color": "#FF6666"},
            {"min": 9,"max": 12, "label": "9-12", "color": "#990033"}
        ]
    )
)
map.render('2022年百强分布地图.html')#2022年

