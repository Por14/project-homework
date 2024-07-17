import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def data_statis():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['font.family']='sans-serif'#设置字体样式
    fig=plt.figure(figsize=(8,5))#生成一张8*5的图
    filename=r'2023年处理后数据.csv'
    #读取CSV文件
    df=pd.read_csv(filename,encoding='ansi')
    df['排名'] = df['排名'].replace('100+', 101)
    #按地区统计各地区的前100学校个数并可视化
    a=df[df['排名'].astype(int)<=100]
    schoolCount=a.groupby('省市').count()
    schoolCount['学校名称'].plot(kind='bar')
    plt.savefig('tu1.png')
    #按学校类型统计各层次学校个数并可视化
    schoolCount=a.groupby('类型').count()
    #print(schoolCount)
    fig=plt.figure(figsize=(8,5))#生成一张8*5的图
    schoolCount['学校名称'].plot(kind='pie',autopct='%1.1f%%')
    plt.savefig('tu2.png')
    #2022年
    fig=plt.figure(figsize=(8,5))#生成一张8*5的图
    filename2=r'2022年处理后数据.csv'
    df=pd.read_csv(filename2,encoding='ansi')
    df['2022排名'] = df['2022排名'].replace('100+', 101)
    b=df[df['2022排名'].astype(int)<=100]
    schoolCount2=b.groupby('省市').count()
    schoolCount2['学校名称'].plot(kind='bar')
    plt.savefig('tu3.png')
    schoolCount2=b.groupby('学校类型').count()
    fig=plt.figure(figsize=(8,5))#生成一张8*5的图
    schoolCount2['学校名称'].plot(kind='pie',autopct='%1.1f%%')
    plt.savefig('tu4.png')
    #折线图
    # 设置中文支持
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题 
    plt.figure(figsize=(8,5))
    x_axis_data = [1,2,3,4,5,6,7,8,9,10]
    y_axis_data1 = [102.8,98.8,98.4,91.7,89.9,87.1,85.5,85.2,84.4,83.9]
    y_axis_data2 = [136.7,102.6,91.4,88.4,82.2,81.7,80.1,79.8,79.1,78.1]
       
    #画图 
    plt.plot(x_axis_data, y_axis_data1, 'b*--', alpha=0.5, linewidth=1, label='2023前十榜')#'
    plt.plot(x_axis_data, y_axis_data2, 'rs--', alpha=0.5, linewidth=1, label='2022前十榜')

    plt.text(1, 109, '山东协和\n学院', ha='center', va='top', fontsize=7)
    plt.text(2, 97.5, '珠海科技\n学院', ha='center', va='top', fontsize=7)
    plt.text(3, 105, '浙江树人\n学院', ha='center', va='top', fontsize=7)
    plt.text(4, 98.5, '武汉东湖\n学院', ha='center', va='top', fontsize=7)
    plt.text(5, 96.5, '黄河科技\n学院', ha='center', va='top', fontsize=7)
    plt.text(6, 94, '齐鲁理工\n学院', ha='center', va='top', fontsize=7)
    plt.text(7, 89, '西京学院', ha='center', va='top', fontsize=7)
    plt.text(8, 91.5, '大连东软\n信息学院', ha='center', va='top', fontsize=7)
    plt.text(9, 91, '无锡太湖\n学院', ha='center', va='top', fontsize=7)
    plt.text(10, 90, '武昌理工\n学院', ha='center', va='top', fontsize=7)

    plt.text(1, 144, '吉首外国语\n大学', ha='center', va='top', fontsize=7)
    plt.text(2, 109, '山东协和\n学院', ha='center', va='top', fontsize=7)
    plt.text(3, 90, '大连东软\n信息学院', ha='center', va='top', fontsize=7)
    plt.text(4, 86, '珠海科技\n学院', ha='center', va='top', fontsize=7)
    plt.text(5, 80, '成都锦城\n学院', ha='center', va='top', fontsize=7)
    plt.text(6, 80, '广洲南方\n学院', ha='center', va='top', fontsize=7)
    plt.text(7, 78, '武昌首义\n学院', ha='center', va='top', fontsize=7)
    plt.text(8, 77.5, '齐鲁理工\n学院', ha='center', va='top', fontsize=7)
    plt.text(9, 77, '武汉东湖\n学院', ha='center', va='top', fontsize=7)
    plt.text(10, 76, '文华学院', ha='center', va='top', fontsize=7)

    plt.legend()  #显示上面的label

    plt.xlabel('排名')
    plt.ylabel('总分')#accuracy
    # 设置横坐标间距为1
    plt.xticks(np.arange(1, len(x_axis_data) + 1, 1))

    plt.ylim(50,150)#仅设置y轴坐标范围
    plt.savefig('tu5.png')
# #双柱图
#     filename2=r'2022年处理后数据.csv'
    #     #读取CSV文件
    #     df2=pd.read_csv(filename2,encoding='ansi')
    #     x = df['']
#     y = df['']
#     # 设置Y轴标签
#     plt.yticks(range(len(y)), df['省市'])
#     # 生成双柱图
#     plt.barh(range(len(y)), -x, color='lightblue', label='2022年', height=0.5)
#     plt.barh(range(len(x)), y, color='pink', label='2023年', height=0.5)
#     # 添加图例
#     plt.legend(loc='upper right')
#     # 显示图表
#     plt.show()


    tk.messagebox.showinfo('保存文件','文件:统计后图片文件保存成功')


