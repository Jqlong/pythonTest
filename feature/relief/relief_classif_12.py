import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_regression

# 读取Excel表格数据
data = pd.read_excel('../relief/all_lose_new.xls')

# 获取特征列和类别列
features = data.iloc[:, :-1]
labels = data.iloc[:, -1]

# 将类别列转化为数字标签
unique_labels = np.unique(labels)
label_dict = {label: i for i, label in enumerate(unique_labels)}
labels = labels.map(label_dict)

# 计算Relief算法的权重
n_features = len(features.columns)
weights = np.zeros(n_features)
for i in range(len(features)):
    # 获取当前实例的特征和类别
    curr_features = features.iloc[i]
    curr_label = labels.iloc[i]
    # 找到最近的同类实例和异类实例
    same_class = features[labels == curr_label]
    diff_class = features[labels != curr_label]
    nearest_same = same_class.sub(curr_features, axis=1).pow(2).sum(axis=1).idxmin()
    nearest_diff = diff_class.sub(curr_features, axis=1).pow(2).sum(axis=1).idxmin()
    # 更新权重
    weights += np.abs(curr_features - features.loc[nearest_same]) - np.abs(curr_features - features.loc[nearest_diff])
weights /= len(features)

# 将权重排序并输出
sorted_features = [x for x, _ in sorted(zip(features.columns, weights), key=lambda x: x[1], reverse=True)]

# 计算特征互信息矩阵
mi_matrix = np.zeros((n_features, n_features))
for i, f1 in enumerate(sorted_features):
    for j, f2 in enumerate(sorted_features[i+1:], start=i+1):
        X = features[[f1] + [f2]].values
        mi = mutual_info_regression(X, labels)
        mi_matrix[i, j] = mi[0, 1]
        mi_matrix[j, i] = mi[0, 1]
np.fill_diagonal(mi_matrix, 1)
# 将互信息矩阵保存到 Excel 文件中
mi_df = pd.DataFrame(mi_matrix, columns=sorted_features, index=sorted_features)
mi_df.to_excel('mi_matrix.xlsx', index=True)
