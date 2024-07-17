import pandas as pd
import numpy as np
import tkinter as tk
def datapress():
    filename=r'csvfile1.csv'
    df=pd.read_csv(filename,encoding='ansi')
    #df['总分'] = df['总分'].astype(str).str.replace('/', None)
    df.dropna()
    df.to_csv('2023年处理后数据.csv',encoding='ansi',index=0)
    #tk.messagebox.showinfo('保存文件','文件：处理后数据1.csv保存成功！')
    #2022
    with open('csvfile2.csv', 'r', encoding='ansi') as infile:
        with open('2022年处理后数据.csv', 'w', encoding='ansi') as outfile:
            for i in range(7):
                next(infile)  # 跳过前六行
            for i, line in enumerate(infile, start=1):  # 从1开始计数，以获取行号
                if i <= 209:  # 如果行号小于或等于209，则写入新文件
                    outfile.write(line)
                else:
                    break  # 如果行号大于209，则跳出循环
    tk.messagebox.showinfo('保存文件','文件：2023年处理后数据.csv保存成功！\n文件：2022年处理后数据.csv保存成功！')

    
