import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import feature.relief_3x as fr3
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

data = pd.read_csv('../relief/all_lose_new.csv', encoding='gbk')

# 特征
# X = data.iloc[:, 2:3]
# x = data['ROTT']
# X = pd.DataFrame(x)
# print(type(X))
# print(X)
# # 类别
# y = data.iloc[:, -1]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 训练模型
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train, y_train)

# 选取特征不同的
mm = fr3.Relief(data, 1, 0.2, 2).reliefF()
# 获取到了权重的排序pandas.core.series.Series
print(mm)
# 获取索引的值
print('-----------------------------------------------------------------')
feature = mm.index[:]
acc = []
print(len(feature))
for i in range(len(feature)):  # 遍历所有值  切片  这是个列表
    # 现在是要每次加一个特征上去
    list_res = list(feature[0:i + 1])
    x = data[list_res]
    X = pd.DataFrame(x)
    print(X)
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    acc_1 = knn.score(X_test, y_test)
    acc.append(acc_1)
print(acc)
list_x = range(1, 18)
print(list_x)
plt.plot(list_x, acc)
plt.xticks(ticks=list_x, labels=None)
plt.show()




