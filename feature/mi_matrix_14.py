# coding=utf-8
import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_classif
from sklearn import metrics

input_file = 'relief/all_lose_new.csv'
df = pd.read_csv(input_file, encoding='gbk')
y = df.iloc[:, -1].values

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
top_12_features = mm.index[:14]
print(top_12_features)
mi_matrix = np.zeros((len(top_12_features), len(top_12_features)))
# print(mi_matrix)
List = []
for i in range(len(top_12_features)):
    A = []
    for j in range(len(top_12_features)):
        feature_1 = top_12_features[i]
        feature_2 = top_12_features[j]
        # mi = mutual_info_classif(df[[feature_1, feature_2]], y)
        mi = metrics.normalized_mutual_info_score(df[feature_1], df[feature_2])
        # mi_matrix[i][j] = mi[0]
        # mi_matrix[j][i] = mi[0]
        A.append(round(mi, 6))
    List.append(A)
# np.fill_diagonal(mi_matrix, 1)
# mi_matrix.to_excel('mi_matrix_new.xlsx')
mi_df = pd.DataFrame(List, columns=top_12_features, index=top_12_features)
# mi_df.to_excel("matrix_14_fea.xlsx")
mi_df.to_excel("matrix_14_fea_new.xlsx")
# print(mi_matrix)
print(mi_df)


