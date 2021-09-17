# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:54:49 2020

@author: vector
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm #cm为matplotlib库中内置的色彩映射函数
import pandas as pd #导入pandas模块，用于读取保存在excel中的岩石样本数据
import numpy as np

fig, ax = plt.subplots(figsize=(7.2,5.4)) #fig代表绘图窗口(Figure)；
#ax代表这个绘图窗口上的坐标系(axis)；a为图形的宽， b为图形的高，单位为英寸

# plot vertical line (from left to right)
plt.vlines(41, 0, 7, linewidth=0.6) #vlines：绘制竖线，41为x坐标，0、7分别为竖线
#的起始y坐标数值；linewidth：指定线宽
plt.vlines(45, 0, 5, linewidth=0.6)
plt.vlines(52, 0, 5, linewidth=0.6)
plt.vlines(52.5, 14, 18, linewidth=0.6)
plt.vlines(57, 0, 5.9, linewidth=0.6)
plt.vlines(63, 0, 7, linewidth=0.6)

#plot horizontal line (from bottom to top)
plt.hlines(3, 37, 45, linewidth=0.6)
plt.hlines(5, 45, 52, linewidth=0.6)
plt.hlines(18, 52.5, 57, linewidth=0.6)

#plot other line (from outside to inside)
plt.plot([37,35],[3,9], #37、35分别是该直线的起始x坐标，3、9分别是起始y坐标
         [35,37],[9,14],
         [37,52.5],[14,18],
         [57,71.8],[18,13.5],
         [71.8,85.9],[13.5,6.8],
         [85.9,87.5],[6.8,4.7],
         [87.5,77.3],[4.7,0],
         [77.3,69],[0,8],
         [69,52],[8,5],
         [69,71.8],[8,13.5],
         [71.8,61],[13.5,8.6],
         [63,61],[16.2,13.5],
         [61,45],[13.5,5],
         [52.5,41],[14,7],
         [52.5,57.6],[14,11.7],
         [57.6,63],[11.7,7],
         [48.4,53],[11.5,9.3],
         [53,57],[9.3,5.9],
         [45,49.4],[9.4,7.3],
         [49.4,52],[7.3,5],
        )

for line in ax.get_lines():
    line.set_color('k')
    line.set_linewidth(0.6)

#读取八个区域的岩石样本数据
rock_df = pd.read_excel('rock data.xlsx') #读取数据文件rock data.xlsx
x = rock_df['SIO2(WT%)'] #读取列标题为“SIO2(WT%)”数据存储到变量x
y = rock_df['NA2O(WT%)'] + rock_df['K2O(WT%)'] #计算全碱
loc = rock_df['Location']
places = ['Place1',
          'Place2',
          'Place3',
          'Place4',
          'Place5',
          'Place6',
          'Place7',
          'Place8',]    


for i, name in zip(range(len(places)),places):
    color = cm.nipy_spectral(float(i+0.9) / len(places))
    plt.scatter( 
        x[loc==name], 
        y[loc==name], #仅绘制地点名为name时的数据点
        color=color, #设置点的颜色
        label=name, #给对应点添加图例名称
        s=60, #设置点的大小
        alpha=0.8, #设置透明度
        zorder=100
    )

#添加横纵坐标轴标签，添加图例
plt.xlabel(r'$\mathrm{SiO_2}$' + ' (wt.%)', 
           fontsize=18, 
          )
plt.ylabel(r'$\mathrm{Na_2O+K_2O}$' +  ' (wt.%)', 
           fontsize=18, 
          )
plt.legend(
        loc='upper right', #图例位置
        shadow=True, #开启阴影
        scatterpoints=1, #图例点数量
        fontsize=10 #字号
        )


plt.xlim(40, 60) #设定x轴坐标范围
plt.ylim(0, 14) #设定y轴坐标范围
new_ticks = np.linspace(40,60,11) 
plt.xticks(new_ticks) #设置x轴刻度分布
ax.tick_params(labelsize=13) #设置刻度标签的大小
ax.tick_params(which='major', direction='in') #坐标轴主要刻度线方向设置为向内
ax.spines['top'].set_linewidth(1) 
ax.spines['right'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1) #设置边框线宽

plt.savefig('TAS.eps')
