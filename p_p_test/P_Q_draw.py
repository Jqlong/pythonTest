import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np

import statsmodels.api as sm

n = 100
samples = st.norm.rvs(loc = 5, scale = 2, size = n)
samples_sort = sorted(samples)

print(samples_sort)
print(len(samples_sort))

probplot = sm.ProbPlot(samples, dist = st.norm, loc = 5, scale = 2)
probplot.qqplot(line='45')


print(type(samples))
print(type(samples_sort))

x_labels_q = samples_sort
y_labels_q = st.norm.ppf(x_labels_q, loc = 5, scale = 2)
plt.scatter(x_labels_q, y_labels_q)
plt.title('QQ plot for normal distribution samle')
plt.show()

x_labels_p = np.arange(1/(2*n), 1, 1/n)
# 传入已经排好序的列表
y_labels_p = st.norm.cdf(samples_sort, loc = 5, scale = 2)
plt.scatter(x_labels_p, y_labels_p)
plt.title('PP plot for normal distribution samle')
plt.show()







