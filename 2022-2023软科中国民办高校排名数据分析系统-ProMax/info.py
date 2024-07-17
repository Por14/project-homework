import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter.messagebox import *
def dataInfo(databox):
    filename=r'2023年处理后数据.csv'
    try:
        df=pd.read_csv(filename,encoding='ansi')
        df1=df.head(10)#显示前十名高校信息


        df1_rows=df1.to_numpy().tolist()
          # 清除当前树形控件的内容
        databox.delete(*databox.get_children())
        title=['1','2','3','4','5']
        column=['排名','学校名称','省市','类型','总分']
        for col in title:
            databox.column(col,width=90,anchor='center')
            i=0
        for colu in column:
                databox.heading(title[i],text=colu)
                i+=1
        for row in df1_rows:
                databox.insert('','end',values=row)
    except FileNotFoundError:
        showinfo("提示", "文件未找到，请检查文件路径是否正确。")
    except Exception as e:
        showinfo("提示", f"发生错误：{e}")
 
def dataInfo2(databox):
    filename=r'2022年处理后数据.csv'
    try:
        df=pd.read_csv(filename,encoding='ansi')
        df1=df.head(10)#显示前十名高校信息


        df1_rows=df1.to_numpy().tolist()
          # 清除当前树形控件的内容
        databox.delete(*databox.get_children())
        title=['1','2','3','4','5']
        column=['排名','学校名称','省市','学校类型','总得分']
        for col in title:
            databox.column(col,width=90,anchor='center')
            i=0
        for colu in column:
                databox.heading(title[i],text=colu)
                i+=1
        for row in df1_rows:
                databox.insert('','end',values=row)
    except FileNotFoundError:
        showinfo("提示", "文件未找到，请检查文件路径是否正确。")
    except Exception as e:
        showinfo("提示", f"发生错误：{e}")

 

