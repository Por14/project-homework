import tkinter
from PIL import Image, ImageTk
from tkinter.messagebox import *
import main


index = tkinter.Tk()  #创建主窗口
# index.attributes('-alpha',1)  #窗口背景透明化
index.title('登录界面') #设置主窗口标题
index.geometry('500x400') #设置主窗口大小
#下面两行代码的作用是固定窗口大小，不可拉动调节
index.maxsize(500,300)
index.minsize(500,300)

# # 加载图片
# canvas = tkinter.Canvas(index, width=500, height=300, bg=None)
# image_file = tkinter.PhotoImage(photo)
# image = canvas.create_image(250, 0, anchor='n', image=image_file)
# canvas.pack()
image = Image.open("VCG211409224266.jpeg")  # 使用Pillow打开图像文件
photo = ImageTk.PhotoImage(image)  # 将Pillow图像转换为Tkinter兼容的PhotoImage

label = tkinter.Label(index, image=photo)
label.image = photo  # 引用保持，防止被垃圾回收
label.place(x=0, y=0, relwidth=1, relheight=1)  # 使用place方法定位图像

#账号与密码文字标签
account_lable = tkinter.Label(index, text = '账号', bg='PaleTurquoise', fg='black', font=('Arial', 12), width=5, height=1)
account_lable.place(relx=0.29,rely=0.4)
pasw_lable = tkinter.Label(index, text = '密码', bg='PaleTurquoise', fg='black', font=('Arial', 12), width=5, height=1)
pasw_lable.place(relx=0.29,rely=0.5)

#账号与密码输入框
account = tkinter.Entry(index,width=20,highlightthickness = 1,highlightcolor = 'lightskyblue',relief='groove')  #账号输入框
account.place(relx=0.4,rely=0.4 )  #添加进主页面,relx和rely意思是与父元件的相对位置
password = tkinter.Entry(index,show='*',highlightthickness = 1,highlightcolor = 'lightskyblue',relief='groove')  #密码输入框
password.place(relx=0.4,rely=0.5) #添加进主页面

user = {"5423":"123","54230405":"abc"}  #定义一个字典来存储用户的信息(key :账号 , value：密码)


#登录按钮处理函数
def login():
    ac = account.get()
    ps = password.get()
    if (ac == "" or ps == ""):
        showinfo("用户登录", "请完整填写信息:)")  # messagebox的方法
    elif user.get(ac) != ps:
        account.delete(0,'end')  #清空文本框的内容
        password.delete(0,'end')  #清空文本框的内容
        showinfo("用户登录", "账号或者密码有误！")   #messagebox的方法
    else:
        account.delete(0, 'end')  # 清空文本框的内容
        password.delete(0, 'end')  # 清空文本框的内容
        showinfo("用户登录", "登录成功！即将进入菜单界面....")  # messagebox的方法
        index.destroy()
        main.do_main()


def reguest():
    ac = account.get()
    ps = password.get()
    if (ac == "" or ps == ""):
        showinfo("用户登录", "请完整填写信息:)")  # messagebox的方法
    elif ac in user:
        account.delete(0,'end')  #清空文本框的内容
        password.delete(0,'end')  #清空文本框的内容
        showinfo("用户注册", "账号已存在！")   #messagebox的方法
    else:
        user[ac] = ps
        account.delete(0, 'end')  # 清空文本框的内容
        password.delete(0, 'end')  # 清空文本框的内容
        showinfo("用户注册", "注册成功！")  # messagebox的方法
#登录与注册按钮
loginBtn = tkinter.Button(index,text='登录',font = ('宋体',12),width=4,height=1,command=login,relief='solid',bd = 0.5,bg='lightcyan')
loginBtn.place(relx=0.41,rely=0.63)
loginBtn = tkinter.Button(index,text='注册',font = ('宋体',12),width=4,height=1,bd=0.5,command=reguest,relief='solid',bg='lightcyan')
loginBtn.place(relx=0.56,rely=0.63)
# 打开主页面函数


# 创建一个Label控件作为标题
label = tkinter.Label(index, text="2022-2023年\n软科中国民办高校排名数据分析系统", font=('Microsoft YaHei', 18, 'bold'), width=30, anchor='center', bg=index.cget('bg'))
label.pack(pady=20)  # 使用pack布局管理器
# 添加注释内容
# label_note = tkinter.Label(index, text="注:为示例\n用户名<5423>,密码<123>",fg="gray")
# label_note.pack(side=tkinter.RIGHT, padx=10, pady=10)  # 使用pack布局管理器


#**************************************************
index.mainloop() #使窗口不断刷新