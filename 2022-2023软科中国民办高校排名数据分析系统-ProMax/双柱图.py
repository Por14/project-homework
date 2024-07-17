 
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # windows系统
plt.rcParams['axes.unicode_minus']=False      #正常显示符号
fig=plt.figure(figsize=(8,5))
x=np.array([2,2,1,7,3,1,8,10,1,10,1,2,2,4,12,2,1,7,1,4,5,6,5,1]) ##2022     
y=np.array([1,2,1,6,4,1,7,14,2,11,2,3,4,5,10,1,1,9,2,4,3,3,6,1])  #2023

plt.ylim(-1,25)
plt.xlim(-16,16)
plt.yticks((-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23),
           ('','上海市','云南省','北京市','吉林省','四川省','宁夏回族','安徽省','山东省','山西省','广东省','广西壮族','江苏省',
            '江西省','河北省','河南省','浙江省','海南省','湖北省','湖南省','福建省','辽宁省','重庆市','陕西省','黑龙江省'))
plt.xticks((-16,-14,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,12,14,16),
           ('-16','-14','-12','-10','-8','-6','-4','-2','0','2','4','6','8','10','12','14','16'))
plt.axvline(0, color='black', linestyle='-',linewidth=2)
plt.barh(range(len(y)), -x,color='lightblue',label='2022年',height=0.5)
plt.barh(range(len(x)), y,color='pink',label='2023年',height=0.5)

plt.legend(loc='upper right')
# plt.show()#legend(loc='upper right')

plt.savefig('tu6.png')




