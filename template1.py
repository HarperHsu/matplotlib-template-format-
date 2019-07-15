# 导入对应库
import matplotlib.pyplot as plt 
import numpy as np 
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#导入数据
# input_txt = 'demo.txt'
# x = [] # 空数组
# y1 = [] # 空数组
# y2 = [] # 空数组
# f = open(input_txt)
# 
# for line in f:
# 	line = line.strip('\n') # 移除回车
# 	line = line.split(' ') # 字符切片，将数据分开
# 	x.append(float(line[0])) # append() 方法用于在列表末尾添加新的对象,用于生成新数组
# 	y1.append(float(line[1]))
# 	y2.append(float(line[2]))
# fclose
# 导完数据

# 或者直接输入数据
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 2, 3, 4]
y2 = [0, 2, 4, 6, 8]
# 赋完数据

# 设置图片figure
figsize = 3.5, 2.625 # 图纸大小3.5x2.625
figure, ax = plt.subplots(figsize=figsize)

# 设置坐标格，四条边粗细
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)

# 设置网格
plt.grid(linestyle='-.', linewidth = 0.5, color = '#000000', which="major") # 可仅显示横纵网格，如添加axis="x"就只显示横网格，颜色表示的几种方式，a:用全名  b:16进制如：#FF00FF  c：RGB或RGBA元组（1,0,1,1） d：灰度强度如：‘0.7’

# 在同一幅图片上画两条折线
A, = plt.plot(x, y1, '-r', linewidth=2.0, label = 'demo1') # '-'为实线,label = 'demo1'为这条线的名字，A为句柄，后面图例用来引用,逗号必须加“A，”
B, = plt.plot(x, y2, 'b-.', linewidth=2.0, label = 'demo2') # '-.'为虚线

# 设置图例
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 14,} # 设置字体
legend = plt.legend(handles=[A, B], prop=font1, loc='upper left') # 添加对应图例 图例位置（upper left指左上角）

# 坐标轴，首先刻度范围啥的
plt.yticks(fontproperties = 'Times New Roman', size = 14) # 刻度的字体和大小
plt.xticks(fontproperties = 'Times New Roman', size = 14)
x_ticks = np.arange(0, 5, 1)
y_ticks = np.arange(0, 10, 2)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.xlim((0, 5)) # 范围
plt.ylim((0, 10))

# 坐标名啥的
plt.xlabel('Voltage (mV)', font1)
plt.ylabel('Current ($\mu$A)', font1) # \mu这里用的Latex格式

# 加标记线箭头啥的
plt.annotate(s = '这里', weight = 'normal', size = 14, color='k', xy=(2,4), xytext=(3,2.5), arrowprops = dict(width = 2, headwidth = 8, headlength = 10, shrink = 0.1, color='k'))
# "s"标注文字(这里试了一下中文)，xy指向的位置点， xytext，shrink指从两端收缩的总长的百分比（调线段长度），arrowprops也可尝试dict(arrowstyle='-|>',color='k')

# 画图
plt.savefig('fig.jpg') # 取消注释即可保存图片
plt.show()