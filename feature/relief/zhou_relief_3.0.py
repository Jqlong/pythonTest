import pandas as pd
import numpy as np

# 3.0数据集

def load_data(filename):
    # 读取数据集
    df = pd.read_csv(filename, encoding='utf-8')

    # 将数据集分成特征和标签两个部分
    X = df.drop(['类别'], axis=1).values
    y = df['类别'].values

    return X, y


def relief(X, y, k=3):
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)

    # 对于每个样本，计算它与其它所有样本之间的距离，然后选取距离最近的k个样本作为该样本的邻居
    for i in range(n_samples):
        dist = np.sum((X - X[i]) ** 2, axis=1)
        nn_index = np.argsort(dist)[1:k + 1]
        nn_labels = y[nn_index]

        # 计算特征权重
        for j in range(n_features):
            f_k = X[i, j]
            near_hit = nn_labels[nn_labels == y[i]]
            near_miss = nn_labels[nn_labels != y[i]]
            hit_diff = np.sum(np.abs(f_k - X[nn_index[nn_labels == y[i]], j]))
            miss_diff = np.sum(np.abs(f_k - X[nn_index[nn_labels != y[i]], j]))
            weights[j] += miss_diff - hit_diff

    # 将所有特征的权重按照从大到小的顺序排序
    indices = np.argsort(weights)[::-1]
    feature_rank = [(i, weights[i]) for i in indices]

    return feature_rank


if __name__ == '__main__':
    # 加载数据集
    X, y = load_data('../relief/watermelon.csv')

    # 计算特征权重并排序
    feature_rank = relief(X, y)

    # 输出特征权重列表
    print('Feature weights:')
    for f, w in feature_rank:
        print('\tFeature %d: %f' % (f, w))

