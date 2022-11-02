import numpy as np
import matplotlib
from pylab import mpl
import matplotlib.pyplot as plt
from scipy.stats import norm
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

"""绘制直方图和拟合曲线"""

mu1, mu2, sigma = 120, 130, 15
x1 = mu1 + sigma * np.random.randn(10000)
# x2 = mu2 + sigma*np.random.randn(10000)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
n, bins, patches = ax1.hist(x1, bins=50, density=True, edgecolor='r', alpha=0.5)  # 创建柱状图
# n, bins, patches = ax1.hist(x2, bins=50, density=True, color='orange', alpha=0.5, stacked=True)

# 计算均值
mu = np.mean(x1)
# 计算标准差
de = np.std(x1)

y = norm.pdf(bins, mu, de)  # 拟合曲线
plt.plot(bins, y, 'g--')  # y轴曲线
plt.xlabel('x')
plt.ylabel('y')

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('位置信息（米）')
plt.ylabel('出现频次')
fig.suptitle('Histograms', fontsize=14, fontweight='bold')
ax1.set_title('Two Frequency Distributions')

plt.show()
