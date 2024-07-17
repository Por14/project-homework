import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import get
import dataPress
import figureView
import dataStatis
import info
from tkinter.messagebox import*

def do_main():
  def do1():
    get.do_scrip(root)
  def do2():
    dataPress.datapress()
  def do3():
    dataStatis.data_statis()
  def do4():
    figureView.figure_view (root)
  def do5():
    info.dataInfo(databox)
  def do6():
    info.dataInfo2(databox)
  root=tk.Tk()


  # 打开图像文件
  image = Image.open("VCG211409224266.jpeg")
  # 设置图像的透明度，1.0表示完全不透明，0.0表示完全透明
  image.putalpha(int(255 * 0.6))  # 例如，这里设置60%的透明度
  # 将处理后的图像转换为Tkinter兼容的PhotoImage
  photo = ImageTk.PhotoImage(image)
  # 创建一个标签，并将图像设置为标签的背景
  label = tk.Label(root, image=photo)
  label.image = photo  # 引用保持，防止被垃圾回收
  label.place(x=0,y=42)

  root.title('主页面')#设置窗体标题
  root.geometry('900x650+500+200')#设置窗体大小
  label1=tk.Label(root,text='2022-2023年\n软科中国民办高校排名数据分析系统',font=('黑体',20),fg='blue')
  label1.place(x=220,y=40)
  #放置标签对象
  title=['1','2','3','4','5']
  databox=ttk.Treeview(root,columns=title,show='headings')
  #创建 rreevlew 对象
  databox.place(x=200,y=100,width=550,height=400)
  bt1=tk.Button(root,text='数据爬取',command=do1)#创建按伍对象
  bt2=tk.Button(root,text='读文件数据处理',command=do2)
  bt3=tk.Button(root,text='数据统计',command=do3)
  bt4=tk.Button(root,text= '数据可视化',command=do4)
  bt5=tk.Button(root,text='显示2023年前10名学校信息',command=do5)
  bt6=tk.Button(root,text='显示2022年前10名学校信息',command=do6)
  bt1.place(x=50,y=100,width=100,height=60)#放置按纽对象
  bt2.place(x=50,y=200,width=100, height=60)
  bt3.place(x=50,y=300,width=100, height=60)
  bt4.place(x=50,y=400,width=100, height=60)
  bt5.place(x=500,y=500,width=175, height=60)
  bt6.place(x=300,y=500,width=175, height=60)
  root.mainloop ()

