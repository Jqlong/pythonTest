# coding=utf-8
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


# 定义Relief类
class Relief:
    def __init__(self, k=5):
        self.k = k  # 最近邻的个数
        self.weights = None  # 特征权重

    def fit(self, X, y):
        n_samples, n_features = X.shape  # 样本数和特征数
        self.weights = np.zeros(n_features)  # 初始化权重为0
        for i in range(n_samples):  # 遍历每个样本
            r = X[i]  # 选取一个样本r
            near_hit = []  # 存储同类的k个最近邻样本
            near_miss = dict()  # 存储异类的k个最近邻样本，按类别分组
            distance = dict()  # 存储每个样本到r的距离，按类别分组
            for j in range(n_samples):  # 遍历其他样本，计算距离
                if i == j:  # 跳过自身
                    continue
                t = X[j]  # 选取另一个样本t
                d = np.sum(np.abs(r - t))  # 计算r和t的曼哈顿距离
                label = y[j]  # 获取t的标签
                if label not in distance:  # 如果该标签还没有存储过距离，初始化一个列表
                    distance[label] = []
                distance[label].append((d, j))  # 将距离和样本序号存入对应的列表中

            for label, d_list in distance.items():  # 遍历每个类别和对应的距离列表
                d_list.sort(key=lambda x: x[0])  # 按照距离升序排序
                if label == y[i]:  # 如果是同类，取前k个作为near_hit
                    near_hit = d_list[:self.k]
                else:  # 如果是异类，取前k个作为near_miss中对应的类别
                    near_miss[label] = d_list[:self.k]

            for feature in range(n_features):  # 遍历每个特征，更新权重
                diff_hit = 0  # 同类差异累加和初始化为0
                diff_miss = 0  # 异类差异累加和初始化为0
                for d, j in near_hit:  # 遍历同类的k个最近邻样本
                    diff_hit += np.abs(X[j][feature] - r[feature]) / (self.k * n_samples)  # 计算特征维度上的差异并累加

                for label, miss_list in near_miss.items():  # 遍历每个异类和对应的k个最近邻样本
                    for d, j in miss_list:
                        diff_miss += np.abs(X[j][feature] - r[feature]) / (
                                    self.k * n_samples * len(near_miss))  # 计算特征维度上的差异并累加

                self.weights[feature] += diff_miss - diff_hit  # 更新该特征的权重

    def transform(self, X, threshold=0):
        return X[:, self.weights > threshold]  # 根据权重阈值筛选特征


# 加载数据集
# X, y = load_iris(return_X_y=True)
# data = pd.read_csv('../relief/all_lose_new.csv', encoding='gbk')

df = pd.read_csv('../relief/all_lose_new.csv', encoding='gbk')
X = df.iloc[:, :-1].values # 特征矩阵X为除了最后一列之外的所有列
y = df.iloc[:, -1].values # 目标向量y为最后一列
# 创建Relief对象并计算特征权重
relief = Relief()
relief.fit(X, y)
print(relief.weights)

