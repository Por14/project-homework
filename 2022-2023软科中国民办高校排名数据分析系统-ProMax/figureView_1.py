import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

def figure_view1(root1):
    top1=tk.Toplevel(root1)#创建子窗体对象
    top1.title('数据可视化窗体')
    top1.transient(root1)#窗口只置顶root之上
    top1.geometry('800x650+500+300')
def analyze_data(df):
    # 在这里执行分析数据的逻辑
    max_region = df.groupby('省市').size().idxmax()
    max_schools = df[df['省市'] == max_region]
    school_names = max_schools['学校名称'].tolist()
    school_kinds = max_schools['学校类型'].tolist()
    combined_school_info = [f"{name} ({kind})" for name, kind in zip(school_names, school_kinds)]
    school_count = len(school_names)
    messagebox.showinfo('结果',
                        f"学校最多的省份是：{max_region}\n学校数量为：{school_count}\n学校名称和类型如下：\n{'\n'.join(combined_school_info)}")


def on_year_select(event):
    selected_year = year_var.get()
    filename = years[selected_year]

    if filename:
        df = pd.read_csv(filename, encoding='ansi')
        analyze_data(df)
    else:
        pass  # 处理其他逻辑


root = tk.Tk()
root.title('选择数据年份')

years = {'Data': None, '2023': '2023年处理后数据.csv', '2022': '2022年处理后数据.csv'}

year_var = tk.StringVar(root)
year_var.set('Data')

year_label = tk.Label(root, text='选择年份:')
year_label.pack()

year_dropdown = ttk.Combobox(root, textvariable=year_var)
year_dropdown['values'] = list(years.keys())
year_dropdown.bind("<<ComboboxSelected>>", on_year_select)
year_dropdown.pack()

root.mainloop()