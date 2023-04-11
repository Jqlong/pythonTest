# coding=utf-8
from sklearn import metrics
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

"""画图"""
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams["axes.unicode_minus"] = False


def NMI_matrix(dataframe):  # 计算标准化互信息矩阵
    # number = dataframe.columns.size  # 获取df的列数
    number = 17
    List = []
    # Name = []
    Name = ['IATmean',
            'ROTT',
            'ROTT_min_mean',
            'IATmax',
            '临近IAT比值',
            'ROTT_ROTT_min',
            'ROTT_dev',
            'Numloss',
            'ROTT_ROTT_mean_dev',
            'ROTT_ROTT_mean',
            'ROTT_mean',
            'ROTT_min',
            'IAT与最小值比',
            'IAT与平均值比',
            'IATmin',
            'IAT',
            'IAT与最大值比']
    # for n in range(number):
    #     Name.append(dataframe.columns[n])  # 获取dataframe的索引
    for i in range(number):
        A = []
        X = dataframe[Name[i]]  # df.columns[i]获取对应列的索引，df['索引']获取对应列的数值
        for j in range(number):
            Y = dataframe[Name[j]]
            A.append(round(metrics.normalized_mutual_info_score(X, Y), 6))  # 计算标准化互信息
        List.append(A)  # List是列表格式


    # figure, ax = plt.subplots(figsize=(12, 12))
    # sns.heatmap(pd.DataFrame(List, index=Name, columns=Name), square=True, annot=True, ax=ax)  # 画出热力图
    # plt.show()
    # 写文件
    NMI = pd.DataFrame(List, index=Name, columns=Name)
    NMI.to_excel('NMI_matrix_14.xlsx')
    print('NMI(标准化互信息) = \n', NMI)  # 将二维列表转为dataframe格式


if __name__ == '__main__':
    # path = './seaborn-data-master/iris.csv'
    path = '../relief/all_lose_new.csv'

    data = pd.read_csv(path, encoding='gbk')  # 读取csv格式的数据
    # df = data.iloc[:, :4]  # 取前四列数据
    NMI_matrix(data)  # df是dataframe格式,计算df的标准化互信息矩阵
