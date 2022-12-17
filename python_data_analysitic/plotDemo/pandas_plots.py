"""pandas画图"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# 创建一个基础图和两个并排放置的子图。
fig, axes = plt.subplots(nrows=1, ncols=2)
# 使用ravel函数将两个子图分别赋给变量。
ax1, ax2 = axes.ravel()
# 生成一个五行三列的数组（服从正态分布）
data_frame = pd.DataFrame(np.random.rand(5, 3),
                          index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'],
                          columns=pd.Index(['Metric 1', 'Metric 2', 'Metric 3'],
                          name='Metric'))
# 左侧创建条形图
data_frame.plot(kind='bar', ax=ax1, alpha=0.75, title='Bar Plot')
# 使用matplotlib的函数设置x轴和y轴标签的旋转角度和字体大小
plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax1.get_yticklabels(), rotation=0, fontsize=10)
ax1.set_xlabel('Customer')
ax1.set_ylabel('Value')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

# 为箱线图单独创建一个颜色字典。
colors = dict(boxes='DarkBlue', whiskers='Gray', medians='Red', caps='Black')
data_frame.plot(kind='box', color=colors, sym='r.', ax=ax2, title='Box Plot')
plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax2.get_yticklabels(), rotation=0, fontsize=10)
ax2.set_xlabel('Metric')
ax2.set_ylabel('Value')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')

plt.savefig('output/pandas_plot.png', dpi=400, bbox_inches='tight')
plt.show()






