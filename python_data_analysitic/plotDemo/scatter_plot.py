"""散点图"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# 从1开始，15结束，每次增加1
# x为一个数组
x = np.arange(start=1., stop=15., step=1.)
print(x)
y_linear = x + 5. * np.random.randn(14)
print(y_linear)
y_quadratic = x**2 + 10. * np.random.randn(14)
print(y_quadratic)
# 使用numpy的polyfit函数通过两组数据点(x,  y_linear)和(x,  y_quadratic)拟合出一条直线和一条二次曲线#
# 使用poly1d函数根据直线和二次曲线的参数生成一个线形方程和二次方程
fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=1))
fn_quadratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(x, y_linear, 'bo', x, y_quadratic, 'go', x, fn_linear(x), 'b-', x, fn_quadratic(x), 'g-', linewidth=2.)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Scatter Plots Regression Lines')
plt.xlabel('x')
plt.ylabel('f(x)')
# 设置x和y轴的范围
plt.xlim((min(x) - 1., max(x) + 1.))
plt.ylim((min(y_quadratic) - 10., max(y_quadratic) + 10.))
plt.savefig('output/scatter_plot.png', dpi=400, bbox_inches='tight')
plt.show()





