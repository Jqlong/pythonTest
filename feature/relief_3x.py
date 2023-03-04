import pandas as pd
import numpy as np
import numpy.linalg as la
import random
import csv
import matplotlib.pyplot as plt
from joblib.numpy_pickle_utils import xrange

# csdn上的代码
from pandas import Series
from sklearn.feature_selection import mutual_info_classif


class Relief:
    def __init__(self, data_df, sample_rate, t, k):
        self.__data = data_df
        self.__feature = data_df.columns
        self.__sample_num = int(round(len(data_df) * sample_rate))
        self.__t = t
        self.__k = k

    def get_data(self):
        new_data = pd.DataFrame()
        for one in self.__feature[:-1]:
            col = self.__data[one]
            if (str(list(col)[0]).split(".")[0]).isdigit() or str(list(col)[0]).isdigit() or \
                    (str(list(col)[0]).split('-')[-1]).split(".")[-1].isdigit():
                new_data[one] = self.__data[one]

            # print('%s 是数值型' % one)
            else:

                # print('%s 是离散型' % one)
                keys = list(set(list(col)))
                values = list(range(len(keys)))
                new = dict(zip(keys, values))
                new_data[one] = self.__data[one].map(new)
        new_data[self.__feature[-1]] = self.__data[self.__feature[-1]]
        return new_data

    # 返回一个样本的k个猜中近邻和其他类的k个猜错近邻

    def get_neighbors(self, row):
        df = self.get_data()
        row_type = row[df.columns[-1]]
        right_df = df[df[df.columns[-1]] == row_type].drop(columns=[df.columns[-1]])
        aim = row.drop(df.columns[-1])
        f = lambda x: cosSim(np.mat(x.values), np.mat(aim.values))
        # f = lambda x: eulidSim(np.mat(x), np.mat(aim))
        right_sim = right_df.apply(f, axis=1)
        right_sim_two = right_sim.drop(right_sim.idxmin())
        right = dict()
        right[row_type] = list(right_sim_two.sort_values().index[0:self.__k])
        # print list(right_sim_two.sort_values().index[0:self.__k])
        lst = [row_type]
        types = list(set(df[df.columns[-1]]) - set(lst))
        wrong = dict()
        for one in types:
            wrong_df = df[df[df.columns[-1]] == one].drop(columns=[df.columns[-1]])
            wrong_sim = wrong_df.apply(f, axis=1)
            wrong[one] = list(wrong_sim.sort_values().index[0:self.__k])
        print(right, wrong)
        return right, wrong

    # 计算特征权重

    def get_weight(self, feature, index, NearHit, NearMiss):
        # data = self.__data.drop(self.__feature[-1], axis=1)
        data = self.__data
        row = data.iloc[index]
        right = 0
        print('####:', NearHit.values())
        for one in list(NearHit.values())[0]:
            nearhit = data.iloc[one]
            if (str(row[feature]).split(".")[0]).isdigit() or str(row[feature]).isdigit() or \
                    (str(row[feature]).split('-')[-1]).split(".")[-1].isdigit():
                max_feature = data[feature].max()
                min_feature = data[feature].min()
                right_one = pow(round(abs(row[feature] - nearhit[feature]) / (max_feature - min_feature), 2), 2)
            else:
                print('@@:', row[feature])
                print('$$:', nearhit[feature])
                print('-' * 100)
                right_one = 0 if row[feature] == nearhit[feature] else 1
            right += right_one
        right_w = round(right / self.__k, 2)
        wrong_w = 0
        # 样本row所在的种类占样本集的比例
        p_row = round(float(list(data[data.columns[-1]]).count(row[data.columns[-1]])) / len(data), 2)
        for one in NearMiss.keys():
            # 种类one在样本集中所占的比例
            p_one = round(float(list(data[data.columns[-1]]).count(one)) / len(data), 2)
            wrong_one = 0
            for i in NearMiss[one]:
                nearmiss = data.iloc[i]
                if (str(row[feature]).split(".")[0]).isdigit() or str(row[feature]).isdigit() or \
                        (str(row[feature]).split('-')[-1]).split(".")[-1].isdigit():
                    max_feature = data[feature].max()
                    min_feature = data[feature].min()
                    wrong_one_one = pow(round(abs(row[feature] - nearmiss[feature]) / (max_feature - min_feature), 2),
                                        2)
                else:
                    wrong_one_one = 0 if row[feature] == nearmiss[feature] else 1
            wrong_one += wrong_one_one
            wrong = round(p_one / (1 - p_row) * wrong_one / self.__k, 2)
            wrong_w += wrong
        w = wrong_w - right_w
        return w

    # 过滤式特征选择
    def reliefF(self):
        sample = self.get_data()
        # print sample
        m, n = np.shape(self.__data)  # m为行数，n为列数
        score = []
        sample_index = random.sample(range(0, m), self.__sample_num)
        print('采样样本索引为 %s ' % sample_index)
        num = 1
        for i in sample_index:  # 采样次数
            one_score = dict()
            row = sample.iloc[i]
            NearHit, NearMiss = self.get_neighbors(row)
            print('第 %s 次采样，样本index为 %s，其NearHit k近邻行索引为 %s ，NearMiss k近邻行索引为 %s' % (num, i, NearHit, NearMiss))
            for f in self.__feature[0:-1]:
                print('***:', f, i, NearHit, NearMiss)
                w = self.get_weight(f, i, NearHit, NearMiss)
                one_score[f] = w
                print('特征 %s 的权重为 %s.' % (f, w))
            score.append(one_score)
            num += 1
        # sorted(score, reverse=True)
        print('--------------------', score)
        f_w = pd.DataFrame(score)
        print('采样各样本特征权重如下：')
        print(f_w)

        print('平均特征权重如下：')
        mean = f_w.mean()
        mm = mean.sort_values(ascending=False, inplace=False)
        print(mm)
        print('-----------------------------------', type(mm))
        # df = pd.read_csv('relief/all_lose_new.csv', encoding='gbk')
        df = pd.read_csv('../relief/all_lose_new.csv', encoding='gbk')
        y = df.iloc[:, -1].values

        print('这是前12的数据')
        top_12_features = mm.index[:12]
        print(top_12_features)

        # top_12_features_df = df[top_12_features.index]
        # mi_matrix = top_12_features_df.corr(method='spearman')
        mi_matrix = np.zeros((len(top_12_features), len(top_12_features)))
        # print(mi_matrix)
        for i in range(len(top_12_features)):
            for j in range(i + 1, len(top_12_features)):
                feature_1 = top_12_features[i]
                feature_2 = top_12_features[j]
                mi = mutual_info_classif(df[[feature_1, feature_2]], y)
                mi_matrix[i][j] = mi[0]
                mi_matrix[j][i] = mi[0]
        np.fill_diagonal(mi_matrix, 1)
        # mi_matrix.to_excel('mi_matrix_new.xlsx')
        mi_df = pd.DataFrame(mi_matrix, columns=top_12_features, index=top_12_features)
        mi_df.to_excel("mi_matrix_new.xlsx")
        print(mi_matrix)

        # df_mi = pd.DataFrame(mi_matrix, columns=top_12_features, index=top_12_features)
        # df_mi.to_excel('mi_matrix_new.xlsx')

        # mm_cut = mm[0:12]
        # print(mm_cut)
        # 生成特征互信息矩阵

        # print(sorted(f_w.mean()))
        return mm

    def get_final(self):
        f_w = pd.DataFrame(self.reliefF(), columns=['weight'])
        final_feature_t = f_w[f_w['weight'] > self.__t]
        print('*' * 100)
        print(final_feature_t)
        # final_feature_k = f_w.sort_values('weight').head(self.__k)
        # print final_feature_k
        return final_feature_t


# 几种距离求解
# 欧氏距离(Euclidean Distance)
def eulidSim(vecA, vecB):
    return la.norm(vecA - vecB)


# 余弦相似度

def cosSim(vecA, vecB):
    """
    :param vecA: 行向量
    :param vecB: 行向量
    :return: 返回余弦相似度(范围在0-1之间)
    """
    num = float(vecA * vecB.T)
    denom = la.norm(vecA) * la.norm(vecB)
    cosSim = 0.5 + 0.5 * (num / denom)
    return cosSim


# 皮尔逊(皮尔森)相关系数

def pearsSim(vecA, vecB):
    if len(vecA) < 3:
        return 1.0
    else:
        return 0.5 + 0.5 * np.corrcoef(vecA, vecB, rowvar=0)[0][1]


if __name__ == '__main__':
    # with open('relief/watermelon.csv', 'r', encoding='utf-8') as f:
    with open('relief/all_lose_new.csv', 'r', encoding='gbk') as f:
        # data = pd.read_csv(f)[['色泽', '根蒂', '敲击', '纹理', '脐部', '触感', '密度', '含糖率', '类别']]
        data = pd.read_csv(f)[
            ['ROTT', 'ROTT_min', 'ROTT_mean', 'ROTT_dev', 'ROTT_ROTT_mean', 'ROTT_ROTT_min',
             'ROTT_min_mean', 'ROTT_ROTT_mean_dev', 'IAT', 'IATmin',
             'IATmax', 'IATmean', 'IAT与最小值比', 'IAT与最大值比', 'IAT与平均值比', '临近IAT比值', 'Numloss',
             '丢包类别']]
    # print(type(data))
    # print(data)
    # f_csv = csv.reader(f)
    # for row in f_csv:
    # print(row)
    f = Relief(data, 1, 0.2, 2)
    # df = f.get_data()
    # print(type(df.iloc[0]))
    # f.get_neighbors(df.iloc[0])
    mm = f.reliefF()
    print(mm)

    # f.get_final()
