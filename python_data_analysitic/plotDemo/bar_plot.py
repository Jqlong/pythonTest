"""条形图"""
import matplotlib.pyplot as plot
# 使用ggplot样式表来模拟ggplot2风格的图形，ggplot2是一个常用的R语言绘图包。
plot.style.use('ggplot')
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
customers_index = range(len(customers))
sale_amounts = [127, 90, 300, 111, 232]
# 创建基础图
fig = plot.figure()
# 向基础图中添加一个子图，创建一行一列的子图，并使用第一个也是唯一一个子图。
ax1 = fig.add_subplot(1, 1, 1)
# 创建条形图。customer_index：设置条形左侧x轴上的坐标；sale_amounts：设置条形的高度；
# align='center设置条形与标签中间对齐；color=darkblue设置条形的颜色。
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
# 设置刻度线在x的底部，y轴的左侧，使图形的上部和右侧不显示刻度线
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
# 将条形的刻度线标签由客户索引值更改为实际的客户名称；rotation=0表示刻度标签应该是水平的，而不是倾斜一个角度
# fontsize='small'将刻度标签的字体设为小字体。
plot.xticks(customers_index, customers, rotation=0, fontsize='small')
plot.xlabel('Customer Name')
plot.ylabel('Sale Amount')
plot.title('Sale Amount per Customer')
# 第三个参数将四周的空白去掉
plot.savefig('output/bar_plot.png', dpi=400, bbox_inches='tight')
plot.show()







