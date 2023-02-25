import pandas as pd
import numpy as np
import numpy as np
from sklearn.feature_selection import mutual_info_regression

# 读取Excel表格数据
from sklearn.feature_selection import mutual_info_classif

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
sorted_weights = sorted(zip(features.columns, weights), key=lambda x: x[1], reverse=True)
for feature, weight in sorted_weights:
    # print(feature, weight)
    print(feature, round(weight, 5))

# mi_matrix = mutual_info_classif(features, labels)

# 读取数据集
data = pd.read_excel('../relief/all_lose_new.xls')

# 提取特征和类别
X = data.iloc[:, :-1]  # 特征
y = data.iloc[:, -1]  # 类别

# 计算特征互信息矩阵的上三角部分
mi_matrix = mutual_info_classif(X, y)

# 创建对称矩阵
num_features = X.shape[1]
matrix = np.zeros((num_features, num_features))

# 填充矩阵的上三角部分
for i in range(num_features):
    for j in range(i + 1, num_features):
        matrix[i, j] = mi_matrix[j - 1]  # j-1是因为第一个特征的互信息值存储在mi_matrix的第0个位置
        matrix[j, i] = mi_matrix[j - 1]

# 打印特征互信息矩阵
print(matrix)

df = pd.DataFrame(matrix, columns=features.columns, index=features.columns)
df.to_excel('../relief/mi_matrix.xlsx')



# # 打印特征互信息值
# for i in range(len(mi_matrix)):
#     print("Feature %d: %.4f" % (i + 1, mi_matrix[i]))
