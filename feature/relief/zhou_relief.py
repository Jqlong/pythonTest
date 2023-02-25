import pandas as pd
import numpy as np



input_file = ''
# 读取西瓜数据集，其中 1 表示好瓜，0 表示坏瓜
df = pd.read_excel('../relief/all_lose.xls')

# 将好瓜和坏瓜分别存储在两个列表中
good = df[df['丢包类别'] == 1]
bad = df[df['丢包类别'] == -1]

# 初始化特征权重向量
weights = np.zeros(len(df.columns) - 1)

# 重复采样次数
n_samples = 100

# 每次重复采样的实例数
k = 200

for i in range(n_samples):
    # 随机选择一个实例
    instance_index = np.random.choice(len(df), 1)[0]
    instance = df.iloc[instance_index]

    # 计算实例与所有实例的距离
    distances = np.sum(np.square(df.iloc[:, :-1].values - instance[:-1].values), axis=1)

    # 找到比当前实例类别不同的 k 个最近邻
    knn = df.iloc[np.argpartition(distances, k + 1)[:k + 1]]
    knn = knn[knn['丢包类别'] != instance['丢包类别']]

    # 更新特征权重
    for j in range(len(weights)):
        diff_good = np.abs(good.iloc[:, j].mean() - instance[j])
        diff_bad = np.abs(bad.iloc[:, j].mean() - instance[j])
        weights[j] += diff_bad ** 2 - diff_good ** 2

# 将特征权重从大到小排序并输出
features = df.columns[:-1]
sorted_indices = np.argsort(weights)[::-1]
sorted_features = features[sorted_indices]
sorted_weights = weights[sorted_indices]
for i in range(len(sorted_features)):
    print(f"{sorted_features[i]}: {sorted_weights[i]}")
