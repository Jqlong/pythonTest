# coding=utf-8
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
import pandas as pd

data = pd.read_csv('../relief/all_lose_new.csv', encoding='gbk')
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
knn = KNeighborsClassifier()
param_grid = {'n_neighbors': [3, 5, 7, 9, 11], 'weights': ['uniform', 'distance']}

grid_search = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy', n_jobs=-1)

grid_search.fit(X_train, y_train)

print("Best parameters: {}".format(grid_search.best_params_))

# 输出在测试集上的准确率
print("Test set accuracy: {:.2f}".format(grid_search.score(X_test, y_test)))

