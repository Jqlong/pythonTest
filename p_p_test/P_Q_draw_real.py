import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np
import sort_date as sd
import statsmodels.api as sm

# n = 100  # 大小





# samples的属性为numpy.ndarray
# samples = st.norm.rvs(loc = 5, scale = 2, size = n)
# samples_sort的属性为list
# samples_sort = sorted(samples)


samples_test = sd.sort_date()   # 将excel中的数据形成列表 已排序
n = len(samples_test)
# 转换成numpy.ndarray格式
samples_test_array = np.array(samples_test)


print(type(samples_test_array))
print(type(samples_test))


#  ----------------------分割线--------------------


probplot = sm.ProbPlot(samples_test_array, dist=st.norm, loc=5, scale=2)
probplot.qqplot(line='45')

sm.qqplot(samples_test_array, line='45')

x_labels_q = samples_test
y_labels_q = st.norm.ppf(x_labels_q, loc=5, scale=2)
plt.scatter(x_labels_q, y_labels_q)
plt.title('QQ plot for normal distribution samle')
plt.show()

x_labels_p = np.arange(1/(2*n), 1, 1/n)
# 传入已经排好序的列表
y_labels_p = st.norm.cdf(samples_test, loc=5, scale=2)
plt.scatter(x_labels_p, y_labels_p)
plt.title('PP plot for normal distribution samle')
plt.show()







