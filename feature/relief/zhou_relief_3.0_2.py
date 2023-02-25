import pandas as pd
import numpy as np



# 加载西瓜数据集 3.0
df = pd.read_csv('../relief/watermelon.csv', index_col='编号')

# 获取数据集中特征数量
num_features = df.shape[1] - 1

# 初始化权重数组
weights = np.zeros(num_features)

# 初始化样本权重
sample_weights = np.ones(df.shape[0])

# 迭代次数
num_iterations = 100

# Relief算法
for i in range(num_iterations):
    # 随机选取一个样本
    idx = np.random.choice(df.shape[0], 1, p=sample_weights / np.sum(sample_weights))[0]
    sample = df.iloc[idx, :]
    # 计算最近邻和最远邻
    dists = np.sqrt(np.sum((df.iloc[:, :num_features] - sample.iloc[:num_features]) ** 2, axis=1))
    nn_idx = np.argmin(dists)
    nn = df.iloc[nn_idx, :]
    fn_idx = np.argmax(dists)
    fn = df.iloc[fn_idx, :]
    # 更新权重
    for j in range(num_features):
        weights[j] += (sample.iloc[j] - nn.iloc[j]) ** 2 - (sample.iloc[j] - fn.iloc[j]) ** 2

# 归一化权重
weights /= num_iterations

# 输出特征权重
for i in range(num_features):
    print(f"Feature {i}: {weights[i]}")

