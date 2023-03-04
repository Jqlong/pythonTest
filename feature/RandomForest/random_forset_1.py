# -*- coding: utf-8 -*-
import csv
from random import seed
from random import randrange
from math import sqrt
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score

from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def loadCSV(filename):  # 加载数据，一行行的存入列表
    dataSet = []
    with open(filename, 'r') as file:
        csvReader = csv.reader(file)
        head = next(csvReader)
        print(head)
        for line in csvReader:
            # print(len(line))
            dataSet.append(line)
    return dataSet  # 这是一个二维列表


# 除了标签列，其他列都转换为float类型
def column_to_float(dataSet):
    featLen = len(dataSet[0]) - 1  # 行数
    # print(featLen)
    for data in dataSet:
        for column in range(featLen):
            data[column] = float(data[column].strip())


# 这一步的目的在于生成几棵树  即几个基分类器
# 将数据集随机分成N块，方便交叉验证，其中一块是测试集，其他四块是训练集
def spiltDataSet(dataSet, n_folds):  # n_folds = 5
    # print(len(dataSet))
    fold_size = int(len(dataSet) / n_folds)  # len(dataSet)是行号 每一组的大小
    dataSet_copy = list(dataSet)  # 复制一份数据
    dataSet_spilt = []
    for i in range(n_folds):
        fold = []
        while len(fold) < fold_size:  # 这里不能用if，if只是在第一次判断时起作用，while执行循环，直到条件不成立
            index = randrange(len(dataSet_copy))  # 随机生成行号，用于分组
            # 将选择的行加入fold中，fold是一个行fold_size，列60的列表
            fold.append(dataSet_copy.pop(index))  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        dataSet_spilt.append(fold)  # 分组的结果
    # print(dataSet_spilt)
    # print(type(dataSet_spilt))
    return dataSet_spilt  # 得到几块数据集


# 构造数据子集  目的是啥：从切割的数据中构造数据子集
def get_subsample(dataSet, ratio):  # ratio = 1.0
    subdataSet = []
    lenSubdata = round(len(dataSet) * ratio)  # 返回浮点数  随机生成行数
    while len(subdataSet) < lenSubdata:
        index = randrange(len(dataSet) - 1)
        subdataSet.append(dataSet[index])
    # print len(subdataSet)
    return subdataSet  # 形成一个随机的数据子集，行不固定


# 分割数据集
def data_spilt(dataSet, index, value):  # value = row[index] 即行的值
    left = []
    right = []
    for row in dataSet:  # 遍历文件行
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


# 计算分割代价
def spilt_loss(left, right, class_values):
    loss = 0.0
    for class_value in class_values:
        left_size = len(left)
        if left_size != 0:  # 防止除数为零
            prop = [row[-1] for row in left].count(class_value) / float(left_size)
            loss += (prop * (1.0 - prop))
        right_size = len(right)
        if right_size != 0:
            prop = [row[-1] for row in right].count(class_value) / float(right_size)
            loss += (prop * (1.0 - prop))
    return loss


# 选取任意的n个特征，在这n个特征中，选取分割时的最优特征
def get_best_spilt(dataSet, n_features):
    features = []
    class_values = list(set(row[-1] for row in dataSet))
    # print('this is class_value', class_values)
    b_index, b_value, b_loss, b_left, b_right = 999, 999, 999, None, None
    while len(features) < n_features:
        index = randrange(len(dataSet[0]) - 1)
        if index not in features:
            features.append(index)
    # print 'features:',features
    for index in features:  # 找到列的最适合做节点的索引，（损失最小）
        for row in dataSet:
            left, right = data_spilt(dataSet, index, row[index])  # 以它为节点的，左右分支
            loss = spilt_loss(left, right, class_values)
            if loss < b_loss:  # 寻找最小分割代价
                b_index, b_value, b_loss, b_left, b_right = index, row[index], loss, left, right
    # print b_loss
    # print type(b_index)
    # 返回一个字典
    return {'index': b_index, 'value': b_value, 'left': b_left, 'right': b_right}


# 决定输出标签
def decide_label(data):
    output = [row[-1] for row in data]
    return max(set(output), key=output.count)


# 子分割，不断地构建叶节点的过程
def sub_spilt(root, n_features, max_depth, min_size, depth):
    left = root['left']
    # print left
    right = root['right']
    del (root['left'])
    del (root['right'])
    # print depth
    if not left or not right:
        root['left'] = root['right'] = decide_label(left + right)
        # print 'testing'
        return
    if depth > max_depth:
        root['left'] = decide_label(left)
        root['right'] = decide_label(right)
        return
    if len(left) < min_size:
        root['left'] = decide_label(left)
    else:
        root['left'] = get_best_spilt(left, n_features)
        # print 'testing_left'
        sub_spilt(root['left'], n_features, max_depth, min_size, depth + 1)
    if len(right) < min_size:
        root['right'] = decide_label(right)
    else:
        root['right'] = get_best_spilt(right, n_features)
        # print 'testing_right'
        sub_spilt(root['right'], n_features, max_depth, min_size, depth + 1)

        # 构造决策树


# 构造决策树 传入随机行数的子集train，特征数量，树的最大深度，最小
def build_tree(dataSet, n_features, max_depth, min_size):
    # 选取分割的最优特征
    root = get_best_spilt(dataSet, n_features)
    sub_spilt(root, n_features, max_depth, min_size, 1)
    return root


# 预测测试集结果
def predict(tree, row):
    predictions = []
    if row[tree['index']] < tree['value']:
        if isinstance(tree['left'], dict):
            return predict(tree['left'], row)
        else:
            return tree['left']
    else:
        if isinstance(tree['right'], dict):
            return predict(tree['right'], row)
        else:
            return tree['right']
            # predictions=set(predictions)


def bagging_predict(trees, row):
    predictions = [predict(tree, row) for tree in trees]
    return max(set(predictions), key=predictions.count)


# 创建随机森林  train：训练集  test：测试集
def random_forest(train, test, ratio, n_features, max_depth, min_size, n_trees):
    trees = []
    for i in range(n_trees):  # 选取的子集数
        train = get_subsample(train, ratio)  # 从切割的数据集中选取子集 行不固定
        # 生成决策树  将选取的子集
        tree = build_tree(train, n_features, max_depth, min_size)
        # print 'tree %d: '%i,tree
        trees.append(tree)
    # predict_values = [predict(trees,row) for row in test]
    predict_values = [bagging_predict(trees, row) for row in test]
    return predict_values


# 计算准确率
def accuracy(predict_values, actual):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predict_values[i]:
            correct += 1
    return correct / float(len(actual))


if __name__ == '__main__':
    seed(1)
    dataSet = loadCSV('test_data/all_lose_new.csv')
    column_to_float(dataSet)  # dataSet  # 将数据转换成float类型
    n_folds = 5  # 将数据集分成5块 按行分
    # max_depth = 15
    max_depth = 18
    min_size = 1
    ratio = 1.0
    n_features = sqrt(len(dataSet) - 1)
    # n_features = 15
    # n_trees = 10   # 选取子集的数量
    n_trees = 12  # 选取子集的数量
    folds = spiltDataSet(dataSet, n_folds)  # 先是切割数据集 得到五个数据块
    # print(folds)
    scores = []  # 用于保存每个数据集的分类准确率
    for fold in folds:
        train_set = folds[  # 复制数据集
                    :]  # 此处不能简单地用train_set=folds，这样用属于引用,那么当train_set的值改变的时候，folds的值也会改变，所以要用复制的形式。（L[:]）能够复制序列，D.copy() 能够复制字典，list能够生成拷贝 list(L)
        # print(len(train_set))
        # print(len(fold))   # 41
        train_set.remove(fold)  # 选好训练集  每次都会移除一个数据块
        # print(len(train_set))  # 都是4
        # print(len(folds))   # 都是5
        # print(train_set)
        train_set = sum(train_set, [])  # 将多个fold列表组合成一个train_set列表
        # print(train_set)
        # print(len(train_set))  # 都是164
        # print len(train_set)
        test_set = []
        for row in fold:  # 将移除的数据块作为测试数据集
            row_copy = list(row)
            row_copy[-1] = None  # 将最后一列设为none
            # print(row_copy)
            test_set.append(row_copy)  # 生成测试数据集
            # for row in test_set:
            # print row[-1]
        actual = [row[-1] for row in fold]  # 获取每个测试集的最后一列值
        # print(actual)

        # 利用随机森林进行预测 返回一个预测的结果列表，和测试数据进行对比
        # train_set：训练数据集  是移除了一个数据集的结果
        # test_set：测试数据集
        # n_features：特征数
        # max_depth = 15, min_size = 1, n_trees = 10

        predict_values = random_forest(train_set, test_set, ratio, n_features, max_depth, min_size, n_trees)
        # print(predict_values)
        accur = accuracy(predict_values, actual)  # 对比，获取准确率
        scores.append(accur)
    print('Trees is %d' % n_trees)
    print('scores:%s' % scores)
    print('mean score:%s' % (sum(scores) / float(len(scores))))

    train_test_split()
    accuracy = accuracy_score()


    # 网格搜索调参：

    # 加载数据
    # filename = 'test_data/sonar-all-data.csv'
    # dataset = loadCSV(filename)
    # column_to_float(dataset)
    #
    # # 划分训练集和测试集
    # X = np.array(dataset)[:, :-1]
    # y = np.array(dataset)[:, -1]
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    #
    # # 定义需要调参的超参数及其取值范围
    # param_grid = {
    #     'max_depth': [2, 4, 6, 8, 10, 12, 14, 15, 16, 17, 18],
    #     'min_samples_split': [2, 5, 10, 20],
    #     'min_samples_leaf': [1, 2, 4, 8],
    #     'max_samples': [10, 11, 12, 13, 14, 15]
    # }
    #
    # # 创建决策树分类器对象
    # dtc = RandomForestClassifier()
    #
    # # 定义网格搜索对象
    # grid_search = GridSearchCV(dtc, param_grid, cv=10, scoring='accuracy')
    #
    # # 在训练集上进行网格搜索
    # grid_search.fit(X_train, y_train)
    #
    # # 输出最优参数组合和在测试集上的表现指标
    # print('Best Parameters:', grid_search.best_params_)
    # y_pred = grid_search.predict(X_test)
    # print('Accuracy:', accuracy_score(y_test, y_pred))
