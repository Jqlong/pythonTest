import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_classif

# 读取Excel表格数据
data = pd.read_excel('../relief/all_lose_new.xls')

# 获取特征列和类别列
features = data.iloc[:, :-1]
labels = data.iloc[:, -1]

# 计算特征互信息
mi_scores = mutual_info_classif(features, labels)

# 将特征和对应的互信息打包成元组列表
feature_mi_pairs = list(zip(features.columns, mi_scores))

# 将元组列表按互信息从大到小排序
sorted_pairs = sorted(feature_mi_pairs, key=lambda x: x[1], reverse=True)

# 获取排序后的特征名称列表
sorted_features = [pair[0] for pair in sorted_pairs]

# 创建特征互信息矩阵
mi_matrix = np.zeros((len(features.columns), len(features.columns)))

# 填充特征互信息矩阵的上三角部分
for i in range(len(sorted_features)):
    for j in range(i+1, len(sorted_features)):
        mi_matrix[i, j] = mutual_info_classif(features[[sorted_features[i], sorted_features[j]]], labels)[1]
        mi_matrix[j, i] = mi_matrix[i, j]
np.fill_diagonal(mi_matrix, 1)
# 将特征互信息矩阵保存到Excel表格中
df_mi_matrix = pd.DataFrame(mi_matrix, index=sorted_features, columns=sorted_features)
df_mi_matrix.to_excel('../relief/mi_matrix.xlsx')
