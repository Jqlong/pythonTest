"""描述性统计"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf
from statsmodels.formula.api import ols, glm

# 将数据集读入到pandas数据框中
# 分割域为逗号，第一行为标题
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
# 有些标题中包含空格，使用下划线替换
wine.columns = wine.columns.str.replace(' ', '_')
# 默认是5行
print(wine.head(7))
# 显示所有变量的描述性统计量
print(wine.describe())
# 找出唯一值
print(sorted(wine.quality.unique()))
# 计算值的频率
print(wine.quality.value_counts())

# -------------------------------------
"""分组、直方图与t检验"""
# 按照葡萄酒类型显示质量的描述性统计量
# unstack方法将结果重新排列
print(wine.groupby('type')[['quality']].describe().unstack('type'))
# 按照葡萄酒类型显示质量的特定分位数值
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))
# 按照葡萄酒类型查看质量分布
red_wine = wine.loc[wine['type'] == 'red', 'quality']
white_wine = wine.loc[wine['type'] == 'white', 'quality']
sns.set_style("dark")
# print(sns.displot(red_wine, density=True, kde=False, color='red', label="Red wine"))
print(sns.distplot(red_wine, norm_hist=True, kde=False, color="red", label="Red wine"))
print(sns.distplot(white_wine, norm_hist=True, kde=False, color='white', label="White wine"))
# 使用utils继续使用 axlabel()方法
sns.utils.axlabel("Quality Score", "Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()
# 检验红葡萄酒和白葡萄酒的平均质量是否有所不同
# 进行t检验
print(wine.groupby(['type'])[['quality']].agg(['std']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f pvalue: %.4f' % (tstat, pvalue))

# -----------------------------------------------------
"""成对变量之间的关系和相关性"""
# 计算所有变量的相关矩阵
# corr函数可以计算出数据集中所有变量老了之间的线性相关性。
print(wine.corr())


# 从红葡萄酒和白葡萄酒的数据中取出一个“小”样本来绘图
def take_sampel(data_frame, replace=False, n=200):
    return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]


reds_sample = take_sampel(wine.loc[wine['type'] == 'red', :])
whites_sample = take_sampel(wine.loc[wine['type'] == 'white', :])
wine_sample = pd.concat([reds_sample, whites_sample])
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1., 0.)
print(pd.crosstab(wine.in_sample, wine.type, margins=True))
# 查看成对变量之间的关系
sns.set_style("dark")
g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci": False, "x_jitter": 0.25, "y_jitter": 0.25}, hue='type', diag_kind='hist', diag_kws={"bins": 10, "alpha": 1.0}, palette=dict(red='red', white='blue'), markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
print(g)
plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize=14, horizontalalignment='center', verticalalignment='top', x=0.5, y=0.999)
plt.show()

# --------------------------------
# 使用最小二乘法估计进行线性回归
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + ' \
             'residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity '
# 使用公式和数据拟合一个普通最小二乘回归模型
lm = ols(my_formula, data=wine).fit()
# 打印摘要信息
print(lm.summary())
# 打印一个列表
print("\nQuantities you can extract from the result:\n%s" % dir(lm))
print("\nCoefficients:\n%s" % lm.params)
print("\nCoefficients Std Errors:\n%s" % lm.bse)
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
print("\nF-statistic:%.1f P-value:%.2f" % (lm.fvalue, lm.f_pvalue))
print("\nNumber of obs:%d Number of fitted values:%d" % (lm.nobs, len(lm.fittedvalues)))


# ----------------------------------------------------
# 自变量标准化
# 创建一个名为dependent_variable的数据框
dependent_variable = wine['quality']

# 创建一个名为independent_variable的数据框
independent_variable = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]

# 对自变量标准化
# 对每个变量，在每个观测中减去变量的均值
# 并使用结果除以变量的标准差
independent_variable_standardized = (independent_variable - independent_variable.mean() / independent_variable.std())

# 将因变量quality作为一列添加到自变量数据框中
# 创建一个带有标准化自变量的新数据集
wine_standardized = pd.concat([dependent_variable, independent_variable_standardized], axis=1)
lm_standardized = ols(my_formula, data=wine_standardized).fit()
print(lm_standardized.summary())


# ----------------------------------------7.2.7 预测---------------------
# 使用葡萄酒数据集中的前10个观测创建10个“新”观测
# 新观测中只包含模型中使用的自变量
new_observations = wine.loc[wine.index.isin(range(10)), independent_variable.columns]

# 基于新观测中的葡萄酒特性预测质量评分
y_predicted = lm.predict(new_observations)

# 将预测值保留两位小数并打印到屏幕上
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)

