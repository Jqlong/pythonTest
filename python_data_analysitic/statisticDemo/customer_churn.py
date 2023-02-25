import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf

# 将数据读入数据框churn
churn = pd.read_csv('churn.csv', sep=',', header=0)
# 使用两次replace将列标题中的空格替换成下划线，并删除嵌入的单引号。
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]
# 创建心裂churn01
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
print(churn.head())




