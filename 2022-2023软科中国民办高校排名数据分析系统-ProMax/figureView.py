import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from PIL import Image, ImageTk
def setImg(label_img,img_png):
    label_img.configure(image=img_png)
    label_img.image=img_png##设置标签的图片参数
def figure_view(root1):
    top1=tk.Toplevel(root1)#创建子窗体对象
    top1.title('数据可视化窗体')
    top1.transient(root1)#窗口只置顶root之上
    top1.geometry('800x650+500+300')
    #
    # # 打开图像文件
    # image = Image.open("VCG211409224266.jpeg")
    # # 设置图像的透明度，1.0表示完全不透明，0.0表示完全透明
    # image.putalpha(int(255 * 0.6))  # 例如，这里设置60%的透明度
    # # 将处理后的图像转换为Tkinter兼容的PhotoImage
    # photo = ImageTk.PhotoImage(image)
    # # 创建一个标签，并将图像设置为标签的背景
    # label = tk.Label(root1, image=photo)
    # label.image = photo  # 引用保持，防止被垃圾回收
    # label.place(x=0, y=20)

    img1=tk.PhotoImage(file=r'tu1.png')
    img2=tk.PhotoImage(file=r'tu2.png')
    label_img=tk.Label(top1)#创建标签对象
    label_img.place(x=5,y=15)




    def do_setImg1():
        setImg(label_img,img1)
    def do_setImg2():
        setImg(label_img,img2)
    but0=tk.Button(top1,text="按地区统计\n(2023)",command=do_setImg1)
    #but0.pack()
    but0.place(x=260,y=25,width=75, height=40)
    but1=tk.Button(top1,text="按类型统计\n(2023)",command=do_setImg2)
    #but1.pack()
    but1.place(x=560,y=25,width=75, height=40)
    #2022年
    img3=tk.PhotoImage(file=r'tu3.png')
    img4=tk.PhotoImage(file=r'tu4.png')
    #label_img=tk.Label(top1)#创建标签对象
    #label_img.place(x=5,y=15)
    def do_setImg3():
        setImg(label_img,img3)
    def do_setImg4():
        setImg(label_img,img4)
    but2=tk.Button(top1,text="按地区统计\n(2022)",command=do_setImg3)
    but2.place(x=160,y=25,width=75, height=40)
    but3=tk.Button(top1,text="按类型统计\n(2022)",command=do_setImg4)
    but3.place(x=460,y=25,width=75, height=40)
    img5=tk.PhotoImage(file=r'tu5.png')
    def do_setImg5():
        setImg(label_img,img5)
    but2=tk.Button(top1,text="两年前十榜",command=do_setImg5)
    but2.place(x=360,y=45,width=75, height=20)

    img6=tk.PhotoImage(file=r'tu6.png')
    def do_setImg6():
        setImg(label_img,img6)
    but6=tk.Button(top1,text="两年百强榜",command=do_setImg6)
    but6.place(x=360,y=25,width=75, height=20)

     # 创建一个字符串变量来存储选择的值                        2023年
    chosen_region = tk.StringVar(top1)
    #地区获取
    filename=r'2023年处理后数据.csv'
    #读取CSV文件
    df=pd.read_csv(filename,encoding='ansi')
    df['排名'] = df['排名'].replace('100+', 101)
    a=df[df['排名'].astype(int)<100]
    regions=a['省市'].tolist()

      # 对地区列表进行排序和去重
    regions = sorted(set(regions))
    #print(regions)

    def display_schools():
        selected_region = chosen_region.get()
        # 筛选出该省份的学校数量和名字
        schools = df[df['省市'] == selected_region]
        if not schools.empty:
            school_count = len(schools)
            school_names = schools['学校名称'].tolist()
            school_kinds =schools['类型'].tolist()
            # 假设 school_names 和 school_kinds 是两个等长的列表
            combined_school_info = [f"{name} ({kind})" for name, kind in zip(school_names, school_kinds)]
            # 使用 join 方法连接字符串
            messagebox.showinfo("学校信息", f"该省份有 {school_count} 所学校，学校名称和类型如下：\n{'\n'.join(combined_school_info)}")
            #messagebox.showinfo("学校信息", f"该省份有 {school_count} 所学校，学校名称和类型如下：\n{'\n'.join(school)}")
        else:
            messagebox.showerror("错误", "未选择省份,请到下方选择。")

    # 创建一个按钮来显示学校信息
    display_schools_button = tk.Button(top1, text="显示学校信息(2023)", command=display_schools)
    display_schools_button.config(font=('Helvetica', 8)) 
    display_schools_button.place(x=350,y=550,width=100, height=20)

    def calculate_max_universities_by_year():
        year = chosen_year.get()
        if year == '2022':
            max_region = b.groupby('省市').size().idxmax()
            # ... [2022年的代码] ...
        elif year == '2023':
            max_region = a.groupby('省市').size().idxmax()
            # ... [2023年的代码] ...
        messagebox.showinfo('结果', f"{year}年民办学校最多的省份是：{max_region}")

    # 创建一个字符串变量来存储选择的年份
    chosen_year = tk.StringVar(top1)

    # 创建一个Combobox控件来选择年份
    year_combobox = ttk.Combobox(top1, textvariable=chosen_year)
    year_combobox['values'] = ['2022', '2023']  # 设置下拉列表的选项
    year_combobox.place(x=350, y=580, width=100, height=20)

    # 创建一个按钮来显示“最多的省份”
    max_universities_button = tk.Button(top1, text='最多的省份', command=calculate_max_universities_by_year)
    max_universities_button.place(x=260, y=525, width=75, height=40)

    def calculate_max_universities():
        max_region = a.groupby('省市').size().idxmax()
        max_schools = a[a['省市'] == max_region]
        school_names = max_schools['学校名称'].tolist()
        school_kinds =max_schools['类型'].tolist()
        # 假设 school_names 和 school_kinds 是两个等长的列表
        combined_school_info = [f"{name} ({kind})" for name, kind in zip(school_names, school_kinds)]
        school_count = len(school_names)
        messagebox.showinfo('结果', f"民办学校最多的省份是：{max_region}\n大学数量为：{school_count}\n大学名称如下：\n{'\n'.join(combined_school_info)}")
    # 添加按钮，用于计算所含最多大学的省份
    button = tk.Button(top1, text='最多的省份\n(2023)', command=calculate_max_universities)
    #button.pack(side=tk.LEFT)
    button.place(x=260,y=525,width=75, height=40)
    #button.pack(side=tk.BOTTOM,padx=10,pady=10)
    def calculate_min_universities():
        min_region = a.groupby('省市').size().idxmin()
        min_schools = a[a['省市'] == min_region]
        school_names = min_schools['学校名称'].tolist()
        school_kinds =min_schools['类型'].tolist()
        # 假设 school_names 和 school_kinds 是两个等长的列表
        combined_school_info = [f"{name} ({kind})" for name, kind in zip(school_names, school_kinds)]
        school_count = len(school_names)
        messagebox.showinfo('结果', f"民办学校最少的省份是：{min_region}\n大学数量为：{school_count}\n学校名称和类型如下：\n{'\n'.join(combined_school_info)}")
    # 添加按钮，用于计算所含最少大学的省份
    button = tk.Button(top1, text='最少的省份\n(2023)', command=calculate_min_universities)
    #button.pack(side=tk.RIGHT)
    button.place(x=560,y=525,width=75, height=40)
    #button.pack(side=tk.BOTTOM,padx=10,pady=10)
    
#2022年
     # 创建一个字符串变量来存储选择的值                        2022年
    chosen_region2= tk.StringVar(top1)
    #地区获取
    filename2=r'2022年处理后数据.csv'
    #读取CSV文件
    df2=pd.read_csv(filename2,encoding='ansi')
    df2['2022排名'] = df2['2022排名'].replace('100+', 101)
    b=df2[df2['2022排名'].astype(int)<100]
    regions2=b['省市'].tolist()

    # 创建一个Combobox控件
    chosen_region = tk.StringVar()
    combobox = ttk.Combobox(top1, textvariable=chosen_region)
    combobox['values'] = regions  # 设置下拉列表的选项
    combobox.place(x=350,y=580,width=100, height=20)
    # 让Combobox支持搜索功能
    combobox.bind('<KeyRelease>', lambda event: combobox.event_generate('<<ComboboxSelected>>'))
    # 添加注释内容
    label= tk.Label(top1, text="注:请在此处进行\n学校所属省份的选择",fg="gray")
    label.place(x=350,y=600)
    
     # 定义函数来显示选择的省份的学校数量和名字
    def display_schools2():
        selected_region2 = chosen_region.get()
        # 筛选出该省份的学校数量和名字
        schools2 = df2[df2['省市'] == selected_region2]
        if not schools2.empty:
            school_count2 = len(schools2)
            school_names2 = schools2['学校名称'].tolist()
            school_kinds2 =schools2['学校类型'].tolist()
            combined_school_info2 = [f"{name} ({kind})" for name, kind in zip(school_names2,school_kinds2)]
            messagebox.showinfo("学校信息", f"该省份有 {school_count2} 所学校，学校名称和类型如下：\n{'\n'.join(combined_school_info2)}")
        else:
            messagebox.showerror("错误", "未选择省份,请到下方选择。")

    # 创建一个按钮来显示学校信息
    display_schools_button2 = tk.Button(top1, text="显示学校信息(2022)", command=display_schools2)
    display_schools_button2.config(font=('Helvetica', 8))
    display_schools_button2.place(x=350, y=520, width=100, height=20)

    def calculate_max_universities2():
        max_region2 = b.groupby('省市').size().idxmax()
        max_schools2 = b[b['省市'] == max_region2]
        school_names2 = max_schools2['学校名称'].tolist()
        school_kinds2 =max_schools2['学校类型'].tolist()
        combined_school_info2 = [f"{name} ({kind})" for name, kind in zip(school_names2, school_kinds2)]
        school_count2 = len(school_names2)
        messagebox.showinfo('结果', f"民办学校最多的省份是：{max_region2}\n大学数量为：{school_count2}\n大学名称如下：\n{'\n'.join(combined_school_info2)}")
    # 添加按钮，用于计算所含最多大学的省份
    button = tk.Button(top1, text='最多的省份\n(2022)', command=calculate_max_universities2)
    #button.pack(side=tk.LEFT)
    button.place(x=160,y=525,width=75, height=40)
    #button.pack(side=tk.BOTTOM,padx=10,pady=10)
    def calculate_min_universities2():
        min_region2 = b.groupby('省市').size().idxmin()
        min_schools2 = b[b['省市'] == min_region2]
        school_names2 = min_schools2['学校名称'].tolist()
        school_kinds2 =min_schools2['学校类型'].tolist()
        # 假设 school_names 和 school_kinds 是两个等长的列表
        combined_school_info2 = [f"{name} ({kind})" for name, kind in zip(school_names2, school_kinds2)]
        school_count2 = len(school_names2)
        messagebox.showinfo('结果', f"民办学校最少的省份是：{min_region2}\n大学数量为：{school_count2}\n学校名称和类型如下：\n{'\n'.join(combined_school_info2)}")
    # 添加按钮，用于计算所含最少大学的省份
    button = tk.Button(top1, text='最少的省份\n(2022)', command=calculate_min_universities2)
    button.place(x=460,y=525,width=75, height=40)


    top1.mainloop()
