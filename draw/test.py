import numpy as np
import matplotlib.pyplot as plt
def draw(self, name, data):
    mean = np.mean(data)  # 计算均值
    std = np.std(data)  # 计算方差
    data1 = [(x - mean) / std for x in data]  # z-score标准化方法(数据标准化)
    num_bins = 100  # 直方图柱子的数量
    plt.figure(figsize=(20, 8))
    # data数据  num_bins柱子个数 range取值范围[-3.3] rwidth柱子宽度
    n, bins, patches = plt.hist(data1, num_bins, range=[-5, 5], rwidth=0.8, density=0.9, facecolor='blue', alpha=0.5)
    # 直方图函数，x为x轴的值，density=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象
    # print(bins)
    y = self.normfun(bins, np.mean(data1), np.std(
        data1))  # 拟合一条最佳正态分布曲线（方程）y  代替品 ——>>> from scipy.stats import norm  y = norm.pdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--')  # 绘制y的曲线
    plt.xlabel('sepal-length')  # 绘制x轴
    plt.ylabel('Probability')  # 绘制y轴
    plt.title(r'{}  $\mu={}$,$\sigma={}$'.format(name, mean, std))  # 标题
    plt.subplots_adjust(left=0.15)  # 左边距

    out_file = 'out_pic/%s.png' % name
    plt.savefig(out_file, transparent=True, bbox_inches='tight', dpi=200, pad_inches=0.0, set_visiable=False,
                format='png')
    print('画图完成 %s' % out_file)
    # plt.show()

draw(1,2)