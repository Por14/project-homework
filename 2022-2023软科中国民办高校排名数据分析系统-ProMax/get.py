from bs4 import BeautifulSoup
import requests
import csv
import tkinter as tk
import re

def getHTMLText(ur1):
    try:
        myheaders={"user-agent":"Mozilla/5.0"}
        r=requests.get(ur1,timeout=100,headers=myheaders)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
def get_contents(ulist,rurl):
    soup=BeautifulSoup(rurl,'html.parser')
    trs=soup.find_all('tr')
    for tr in trs:
        ui=[]
        list1=tr.find_all('td')
        for td in list1:
            if td.a:
                ui.append(td.a.string)
            else:
                ui.append(td.string)    
        ulist.append(ui)
def save_contents(filename,urlist):
    with open(filename,'w',newline='') as f:
        writer=csv.writer(f)
        writer.writerows(urlist)
        

##子页面
#2023年
urlist=[]
ur1="https://www.maigoo.com/news/662215.html"
filename="csvfile1.csv"
rs=['']
def do1():
    rs[0]=getHTMLText(ur1)
    if rs[0]!='':
        tk.messagebox.showinfo('2023年','获取网页正常！')
def do2():
    get_contents(urlist,rs[0])
    if urlist!='':
        tk.messagebox.showinfo('2023年','获取网页正常！')
def do3():
    save_contents(filename,urlist)
    tk.messagebox.showinfo('2023年','获取网页正常！')
#2022年
urlist2=[]
ur2="https://www.daxuerank.com/thread-546-1-1.html"
filename="csvfile2.csv"
rs=['']
def do4():
    rs[0]=getHTMLText(ur2)
    if rs[0]!='':
        tk.messagebox.showinfo('2022年','获取网页正常！')
def do5():
    get_contents(urlist2,rs[0])
    if urlist2!='':
        tk.messagebox.showinfo('2022年','获取网页正常！')
def do6():
    save_contents(filename,urlist2)
    tk.messagebox.showinfo('2022年','获取网页正常！')



def do_scrip(root1):
    top1=tk.Toplevel(root1)
    top1.title('数据爬取窗体')
    top1.transient(root1)
    top1.geometry('500x500+500+300')
    bt1=tk.Button(top1,text='获取网页内容\n(2023)',command=do1)#创建按伍对象
    bt2=tk.Button(top1,text='获取表格数据\n(2023)',command=do2)
    bt3=tk.Button(top1,text='保存表格数据\n(2023)',command=do3)
    bt1.place(x=50,y=100,width=100,height=60)#放置按纽对象
    bt2.place(x=50,y=175,width=100, height=60)
    bt3.place(x=50,y=250,width=100, height=60)
    bt4=tk.Button(top1,text='获取网页内容\n(2022)',command=do4)#创建按伍对象
    bt5=tk.Button(top1,text='获取表格数据\n(2022)',command=do5)
    bt6=tk.Button(top1,text='保存表格数据\n(2022)',command=do6)
    bt4.place(x=200,y=100,width=100,height=60)#放置按纽对象
    bt5.place(x=200,y=175,width=100, height=60)
    bt6.place(x=200,y=250,width=100, height=60)











