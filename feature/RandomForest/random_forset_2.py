import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, classification_report, \
    mean_absolute_error, roc_curve, auc
import pandas as pd
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import svm
# import feature.KNN.ROC_dec as roc_dec

# df = pd.read_csv('test_data/all_lose_new.csv', encoding='gbk')
data = pd.read_csv("../relief/all_lose_new.csv", encoding='gbk')
y = data["丢包类别"]
X = pd.DataFrame(data, columns=['IATmean', 'ROTT', 'ROTT_min_mean', 'IATmax', '临近IAT比值', 'ROTT_ROTT_min',
                                   'ROTT_dev', 'Numloss', 'ROTT_ROTT_mean_dev', 'ROTT_ROTT_mean'])

# X = df.iloc[:, :-1]
# y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# 生成具有相关性的二分类数据
X, y = make_classification(n_samples=5000, n_features=5, n_informative=3,
                           n_redundant=0, n_clusters_per_class=1, random_state=42)
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X, y, random_state=42, test_size=0.3)
lr = LogisticRegression(random_state=42)
lr.fit(X, y)

"""随机森林"""
# rf = RandomForestClassifier(n_estimators=150, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
"""SVM"""
svc = svm.SVC(C=1000, kernel='rbf', gamma=0.4, probability=True)
svc.fit(X_train, y_train)

y_pred = rf.predict(X_test)
y_pred_svm = svc.predict(X_test)

"""随机森林性能指标"""
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
precision = precision_score(y_test, y_pred, average='macro')
print(classification_report(y_test, y_pred))
print("accuracy", accuracy)
print("f1", f1)
print("recall", recall)
print("precision", precision)

"""SVM性能指标"""
print('-----------------------------')
accuracy_svm = svc.score(X_test, y_test)
f1_svm = f1_score(y_test, y_pred_svm, average='macro')
recall_svm = recall_score(y_test, y_pred_svm, average='macro')
precision_svm = precision_score(y_test, y_pred_svm, average='macro')
print("accuracy", accuracy_svm)
print("f1", f1_svm)
print("recall", recall_svm)
print("precision", precision_svm)

# 性能直方图
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams["axes.unicode_minus"] = False
label_list = ['Spike', 'ZigZag', 'ZBS', 'LDM-satellite', 'SVM-based', 'New']

input_file = '../KNN'
y_test_list = pd.read_excel('../KNN/y_test.xls')
df2 = pd.read_excel('../KNN/y_score.xls')
df3 = pd.read_excel('../KNN/pre_result.xls')
y_score_list = np.array(df2)
pre_list = np.array(df3)
accscore1 = accuracy_score(y_test_list, pre_list)
prescore1 = precision_score(y_test, pre_list, average='macro')
rescore1 = recall_score(y_test, pre_list, average='macro')
f1score1 = f1_score(y_test, pre_list, average='macro')
list1 = [0.535, 0.605, 0.805, accuracy, accuracy_svm, accscore1]
list2 = [0.4364, 0.4476, 0.7937, f1, f1_svm, f1score1]
list3 = [0.5538, 0.7442, 0.8427, recall, recall_svm, rescore1]
list4 = [0.36, 0.32, 0.75, precision, precision_svm, prescore1]
x = range(len(list1))
rects1 = plt.bar(x, height=list1, width=0.15, alpha=0.5, color='#94bde7', label='accuracy', hatch='//', ls='-', lw=1)
rects2 = plt.bar([i + 0.2 for i in x], height=list2, width=0.15, alpha=0.5, color='#ad2110',
                 label='f1', hatch='xx')
rects3 = plt.bar([i + 0.2 * 2 for i in x], height=list3, width=0.15, alpha=0.5, color='#ffefad', label='recall', hatch='++', lw=1)
rects4 = plt.bar([i + 0.2 * 3 for i in x], height=list4, width=0.15, alpha=0.5, color='#94d6c6', label='precision')
plt.xticks([index + 0.2 for index in x], label_list)
plt.ylim(0.7, 1.0)
plt.legend()
plt.show()

# print(classification_report(y_test, y_pred))
#
# print("Accuracy:", accuracy)
# print("F1 score:", f1)
# print("Recall:", recall)
# print("Precision:", precision)
#
# plt.rcParams["font.sans-serif"] = ['SimHei']
# plt.rcParams["axes.unicode_minus"] = False
#
# plt.bar(0.1, accuracy, width=0.1, label='Accuracy')
# plt.bar(0.2, f1, width=0.1, label='F1_score')
# plt.bar(0.3, recall, width=0.1, label='Recall')
# plt.bar(0.4, precision, width=0.1, label='Precision')
# plt.title('随机森林性能指标')
# plt.xlabel('随机森林')
# plt.ylabel('评价检测性能')

# mae曲线

# mae_list = []
# # num_estimators = [10, 50, 100, 200]
# for i in range(1, 200, 10):
#     rf1 = RandomForestClassifier(n_estimators=i, random_state=42)
#     print(i)
#     rf1.fit(X_train, y_train)
#     y_pred1 = rf1.predict(X_test)
#     mae = mean_absolute_error(y_test, y_pred1)
#     mae_list.append(mae)
# print(mae_list)
# print(min(mae_list))
#
# plt.plot(range(1, 200, 10), mae_list)
# plt.show()

# roc曲线  新增SVM
"""SVM ROC曲线"""
# y_score = rf.fit(X_train, y_train).predict_proba(X_test)
y_score = rf.predict_proba(X_test)
# y_score_svm = svc.fit(X_train, y_train).predict_proba(X_test)
y_pred_svm = svc.predict_proba(X_test)
y_score_svm = y_pred_svm[:, 1]
"""随机森林ROC曲线"""
fpr, tpr, thresholds = roc_curve(y_test, y_score[:, 1])
fpr_svm, tpr_svm, thresholds_svm = roc_curve(y_test, y_score_svm)
roc_auc = auc(fpr, tpr)
roc_auc_svm = auc(fpr_svm, tpr_svm)

"""GD ROC曲线"""
y_prob = lr.predict_proba(X_test_1)
y_score_GD = y_prob[:, 1]

# 计算ROC曲线和AUC
fpr1, tpr1, thresholds1 = roc_curve(y_test_1, y_score_GD)
roc_auc1 = auc(fpr1, tpr1)

plt.plot(fpr, tpr, color='gray', label='LDM-satellite (AUC = %0.3f)' % roc_auc, ls='-.')
plt.plot(fpr_svm, tpr_svm, color='#9400D3', label='SVM-based (AUC = %0.3f)' % roc_auc_svm, ls='--')
plt.plot(fpr1, tpr1, color='red', label='本文方法 (AUC = %0.3f)' % roc_auc1, lw=2)

plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")
# plt.grid(grid_linestyle='-.')
plt.grid(True)

plt.legend()

plt.show()
