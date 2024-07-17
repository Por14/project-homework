from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data2 = [
    ("上海市",1),
    ("云南省",2),
    ("北京市",1),
    ("吉林省",6),
    ("四川省",4),
    ("宁夏回族自治区",1),
    ("安徽省",7),
    ("山东省",14),
    ("山西省",2),
    ("广东省",11),
    ("广西壮族自治区",2),
    ("江苏省",3),
    ("江西省",4),
    ("河北省",5),
    ("河南省",10),
    ("浙江省",1),
    ("海南省",1),
    ("湖北省",9),
    ("湖南省",2),
    ("福建省",4),
    ("贵州省",1),
    ("辽宁省",3),
    ("重庆市",3),
    ("陕西省",6),
    ("黑龙江省",1)
]
#添加数据
map.add("2023前一百地区分布图",data2,"china")
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
map.render(('2023年百强分布地图.html'))#2023年
