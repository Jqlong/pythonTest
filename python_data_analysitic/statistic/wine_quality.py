"""葡萄酒质量-描述性统计"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf
from statsmodels.formula.api import ols, glm
# 将数据集读入到pandas数据框中
# 读文件，域分隔为逗号，第一行列标题
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
# 有些标题中包含空格，用_代替
wine.columns = wine.columns.str.replace(' ', '_')
# 数字表示显示多少行，无参默认5行
print(wine.head(6))
# 显示所有变量的描述性统计量
print(wine.describe())
# 找出唯一值
print(sorted(wine.quality.unique()))
# 计算值的频率
print(wine.quality.value_counts())

# 按照葡萄酒类型显示质量的描述性统计量
print(wine.groupby('type')[['quality']].describe().unstack('type'))
# 按照葡萄酒类型显示质量的特定分位数值
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))




