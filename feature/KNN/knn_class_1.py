import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import feature.relief_3x as fr3
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn import svm

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
# mm = fr3.Relief(data, 1, 0.2, 2).reliefF()
# # 获取到了权重的排序pandas.core.series.Series
# print(mm)
mm_m = {'IATmean': 0.031094,
        'ROTT': 0.022750,
        'ROTT_min_mean': 0.017432,
        'IATmax': 0.006748,
        '临近IAT比值': -0.007490,
        'ROTT_ROTT_min': -0.009605,
        'ROTT_dev': -0.009641,
        'Numloss': -0.010733,
        'ROTT_ROTT_mean_dev': -0.012359,
        'ROTT_ROTT_mean': -0.012709,
        'ROTT_mean': -0.013706,
        'ROTT_min': -0.026769,
        'IAT与最小值比': -0.094195,
        'IAT与平均值比': -0.111619,
        'IATmin': -0.235939,
        'IAT': -0.323253,
        'IAT与最大值比': -0.628012}
mm = pd.Series(mm_m)

# 获取索引的值
print('-----------------------------------------------------------------')
feature = mm.index[:]
acc1 = []
acc2 = []
acc3 = []
acc4 = []
print(len(feature))
for i in range(len(feature)):  # 遍历所有值  切片  这是个列表
    # 现在是要每次加一个特征上去
    list_res = list(feature[0:i + 1])
    x = data[list_res]
    X = pd.DataFrame(x)
    print(X)
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    """KNN分类"""
    knn = KNeighborsClassifier(n_neighbors=7, weights='uniform')
    knn.fit(X_train, y_train)
    acc_1 = knn.score(X_test, y_test)
    acc1.append(acc_1)

    """决策树分类"""
    # dec_tree = DecisionTreeClassifier(criterion='gini', max_depth=8)
    dec_tree = DecisionTreeClassifier(criterion='entropy',
                                      max_depth=11,
                                      min_samples_leaf=3,
                                      min_samples_split=29,
                                      splitter='best')
    dec_tree.fit(X_train, y_train)
    y_prep = dec_tree.predict(X_test)
    acc_2 = accuracy_score(y_test, y_prep)
    acc2.append(acc_2)

    """逻辑回归"""
    # logic_reg = LogisticRegression(class_weight='balanced', penalty='l2', multi_class='multinomial')
    logic_reg = LogisticRegression(C=1000, penalty='l2', solver='liblinear')  # 徐
    logic_reg.fit(X_train, y_train)
    y_prep = logic_reg.predict(X_test)
    acc_3 = accuracy_score(y_test, y_prep)
    acc3.append(acc_3)

    """支持向量机"""
    # svc = svm.SVC(C=1.0, kernel='rbf', gamma=10)
    svc = svm.SVC(C=1000, kernel='rbf', gamma=0.4, probability=True)
    svc.fit(X_train, y_train)
    y_pred = svc.predict(X_test)
    acc_4 = accuracy_score(y_test, y_pred)
    acc4.append(acc_4)

    """网格调参 KNN"""
    # knn = KNeighborsClassifier()
    # param_grid = {'n_neighbors': [3, 5, 7, 9, 11], 'weights': ['uniform', 'distance']}
    #
    # grid_search = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy', n_jobs=-1)
    #
    # grid_search.fit(X_train, y_train)
    #
    # print("Best parameters: {}".format(grid_search.best_params_))
    #
    # # 输出在测试集上的准确率
    # print("Test set accuracy: {:.2f}".format(grid_search.score(X_test, y_test)))

    """决策树 调参"""
    # dec_tree = DecisionTreeClassifier(random_state=42)
    # params = {
    #     'criterion': ['gini', 'entropy'],
    #     'max_depth': [2, 4, 6, 8, 10],
    #     'min_samples_split': [2, 4, 6, 8, 10],
    #     'min_samples_leaf': [1, 2, 3, 4, 5],
    #     'max_features': [None, 'sqrt', 'log2']
    # }
    # grid_search = GridSearchCV(dec_tree, params, scoring='accuracy', cv=10, n_jobs=-1)
    # grid_search.fit(X_train, y_train)
    # y_pred = grid_search.predict(X_test)
    # print("Best parameters: {}".format(grid_search.best_params_))
    # print("Test set accuracy: {:.2f}".format(accuracy_score(y_test, y_pred)))

    """逻辑回归 调参"""
    # logic_reg = LogisticRegression(random_state=42)
    # params = {
    #     'penalty': ['l1', 'l2'],
    #     'C': [0.001, 0.01, 0.1, 1, 10, 100],
    #     'class_weight': [None, 'balanced'],
    #     'multi_class': ['auto', 'ovr', 'multinomial'],
    # }
    # grid_search = GridSearchCV(logic_reg, params, scoring='accuracy', cv=10, n_jobs=-1)
    # grid_search.fit(X_train, y_train)
    # y_pred = grid_search.predict(X_test)
    # print("Best parameters: {}".format(grid_search.best_params_))
    # print("Test set accuracy: {:.2f}".format(accuracy_score(y_test, y_pred)))

    """支持向量机 调参"""
    # svc = svm.SVC()
    # params = {
    #     'C': [0.1, 1, 10, 100],
    #     'gamma': [0.1, 1, 10, 100],
    #     'kernel': ['linear', 'rbf', 'sigmoid']
    # }
    # grid_search = GridSearchCV(svc, params, cv=10, scoring='accuracy', n_jobs=-1)
    # grid_search.fit(X_train, y_train)
    # y_pred = grid_search.predict(X_test)
    # print("Best parameters: {}".format(grid_search.best_params_))
    # print("Test set accuracy: {:.2f}".format(accuracy_score(y_test, y_pred)))


print(acc1)
"""KNN准确率"""
acc_num = pd.Series(acc1)
print(acc_num)
print(acc_num.argmax())
print(acc_num.max())
"""决策树准确率"""
print('++++++++++++++++++++++++++++++')
acc_num_2 = pd.Series(acc2)
print(acc_num_2)
print(acc_num_2.argmax())
print(acc_num_2.max())
"""逻辑回归准确率"""
print('******************************')
acc_num_3 = pd.Series(acc3)
print(acc_num_3)
print(acc_num_3.argmax())
print(acc_num_3.max())
"""支持向量机准确率"""
print('------------------------------')
acc_num_4 = pd.Series(acc4)
print(acc_num_4)
print(acc_num_4.argmax())
print(acc_num_4.max())

"""画图"""
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams["axes.unicode_minus"] = False
list_x = range(1, 18)
print(list_x)
# plt.plot(list_x, acc, 'rs-')
# KNN分类算法折线图
plt.plot(list_x, acc1, 's-', markerfacecolor='none', label='KNN', color='#F9A602')
"""决策树折线图"""
plt.plot(list_x, acc2, '*-', label='DT', color='#3399FF')
"""逻辑回归决策树"""
plt.plot(list_x, acc3, 'o-', label='LR', color='#CC7112')
"""支持向量机"""
plt.plot(list_x, acc4, 'd-', label='SVM', color='#13C4A3')
plt.xlabel('特征数量')
plt.ylabel('准确率')
plt.xticks(ticks=list_x, labels=None)
plt.legend()
plt.savefig('accuracy.pdf', format='pdf', bbox_inches='tight')
plt.show()
