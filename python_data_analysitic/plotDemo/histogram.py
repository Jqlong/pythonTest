"""直方图"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
mu1, mu2, sigma = 100, 130, 15
# 使用python的随机数生成器创建两个正态分布变量。
# randn(10000)一个参数，生成秩为一的数组,有10000个数据
x1 = mu1 + sigma * np.random.randn(10000)
print(len(x1))
x2 = mu2 + sigma * np.random.randn(10000)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# 将变量分成50份。
# normed=False表示直方图显示的是频率分布，而不是概率密度
# alpha=0.5表示第二个直方图应该是透明的
n, bins, patches = ax1.hist(x1, bins=50, density=False, color='darkgreen', edgecolor='black')
n, bins, patches = ax1.hist(x2, bins=50, density=False, color='orange', alpha=0.5, edgecolor='red')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
# 添加居中的标题
fig.suptitle('Histograms', fontsize=14, fontweight='bold')
# 为子图添加居中标题
ax1.set_title('Two Frequency Distributions')
plt.savefig('output/histogram.png', dpi=400, bbox_inches='tight')
plt.show()





