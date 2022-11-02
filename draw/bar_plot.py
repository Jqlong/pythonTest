#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']   # 横坐标标签
customers_index = range(len(customers))   # 左侧在x轴上的坐标
sale_amounts = [127, 90, 201, 111, 232]   # 条形的高度
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom')   # 刻度线的位置设在x轴底部和左侧
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, customers, rotation=0, fontsize='small')  # 更改客户刻度线
plt.xlabel('Customer Name')   # 标题
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')
# plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()