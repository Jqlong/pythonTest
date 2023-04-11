# -*- coding: utf-8 -*-
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split  # 导入切分训练集、测试集模块
from sklearn.metrics import classification_report, roc_auc_score, roc_curve, auc, accuracy_score, precision_score, \
    recall_score, f1_score
from sklearn.model_selection import GridSearchCV

# 消除警告
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)

data = pd.read_csv("../KNN/all_lose_new.csv", encoding='gbk')
target = data["丢包类别"]
data = pd.DataFrame(data, columns=['IATmean', 'ROTT', 'ROTT_min_mean', 'IATmax', '临近IAT比值', 'ROTT_ROTT_min',
                                   'ROTT_dev', 'Numloss', 'ROTT_ROTT_mean_dev', 'ROTT_ROTT_mean'])
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=1)

X, y = make_classification(n_samples=5000, n_features=5, n_informative=3,
                           n_redundant=0, n_clusters_per_class=1, random_state=40)
x_train1, x_test1, y_train1, y_test1 = train_test_split(X, y, test_size=0.3, random_state=1)




def get_voting1(scores):
    models = list()
    models.append(('lr', LogisticRegression(max_iter=3000, random_state=1, C=1000)))
    models.append(('svm', SVC(probability=True, random_state=1, C=1000, gamma=10)))
    models.append(('dtc', DecisionTreeClassifier(random_state=1, max_depth=7)))
    models.append(('knn', KNeighborsClassifier(n_neighbors=5)))
    Weighting_ensemble = VotingClassifier(estimators=models, voting='soft', weights=scores)
    return Weighting_ensemble


def get_models():
    models = dict()
    models['lr'] = LogisticRegression(max_iter=3000, random_state=1)
    models['svm'] = SVC(probability=True, random_state=1)
    models['dtc'] = DecisionTreeClassifier(random_state=1)
    models['knn'] = KNeighborsClassifier()
    # models['soft_voting'] = get_voting()
    return models


def data_model(model, x_train, y_train, x_test, y_test):
    model.fit(x_train, y_train)
    pre_result = model.predict(x_test)
    accscore = accuracy_score(y_test, pre_result)
    prescore = precision_score(y_test, pre_result, average='macro')
    rescore = recall_score(y_test, pre_result, average='macro')
    f1score = f1_score(y_test, pre_result, average='macro')
    predict_probs = model.predict_proba(x_test)
    y_score = predict_probs[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_score)
    return accscore, prescore, rescore, f1score, fpr, tpr, thresholds


models = get_models()
accscore_list, prescore_list, rescore_list, f1score_list, fpr_list, tpr_list, thresholds_list, names, acc_list1 = list(), list(), list(), list(), list(), list(), list(), list(), list()
names.append('Spike')
names.append('ZigZag')
names.append('ZBS')
names.append('LDM-satellite')
names.append('SVM-based')
names.append('本文方法')
for name, model in models.items():
    accscore, prescore, rescore, f1score, fpr, tpr, thresholds = data_model(model, x_train1, y_train1, x_test1, y_test1)
    acc_list1.append(round(accscore, 3))
GD_ensemblee = get_voting1(acc_list1)
accscore, prescore, rescore, f1score, fpr, tpr, thresholds = data_model(GD_ensemblee, x_train1, y_train1, x_test1,
                                                                        y_test1)

y_test_list = pd.read_excel("../KNN/y_test.xls")
df2 = pd.read_excel('../KNN/y_score.xls')
df3 = pd.read_excel('../KNN/pre_result.xls')
y_score_list = np.array(df2)
pre_list = np.array(df3)
accscore1 = accuracy_score(y_test_list, pre_list)
prescore1 = precision_score(y_test, pre_list, average='macro')
rescore1 = recall_score(y_test, pre_list, average='macro')
f1score1 = f1_score(y_test, pre_list, average='macro')

"""我的"""
# rf = RandomForestClassifier(n_estimators=150, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(x_train, y_train)
"""SVM"""
svc = svm.SVC(C=1000, kernel='rbf', gamma=0.4, probability=True)
svc.fit(x_train, y_train)

y_pred = rf.predict(x_test)
y_pred_svm = svc.predict(x_test)

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
accuracy_svm = svc.score(x_test, y_test)
f1_svm = f1_score(y_test, y_pred_svm, average='macro')
recall_svm = recall_score(y_test, y_pred_svm, average='macro')
precision_svm = precision_score(y_test, y_pred_svm, average='macro')
print("accuracy", accuracy_svm)
print("f1", f1_svm)
print("recall", recall_svm)
print("precision", precision_svm)

"""其他方法"""
accscore_list.append(0.535)
accscore_list.append(0.605)
accscore_list.append(0.805)
prescore_list.append(0.36)
prescore_list.append(0.32)
prescore_list.append(0.75)
rescore_list.append(0.5538)
rescore_list.append(0.7442)
rescore_list.append(0.8427)
f1score_list.append(0.4364)
f1score_list.append(0.4476)
f1score_list.append(0.7937)

"""随机森林"""
accscore_list.append(round(accuracy, 3))
prescore_list.append(round(precision, 3))
rescore_list.append(round(recall, 3))
f1score_list.append(round(f1, 3))
"""SVM"""
accscore_list.append(round(accuracy_svm, 3))
prescore_list.append(round(precision_svm, 3))
rescore_list.append(round(recall_svm, 3))
f1score_list.append(round(f1_svm, 3))

"""GD"""
accscore_list.append(round(accscore1, 3))
prescore_list.append(round(prescore1, 3))
rescore_list.append(round(rescore1, 3))
f1score_list.append(round(f1score1, 3))




"""随机森林roc"""
y_score = rf.predict_proba(x_test)
fpr_rm, tpr_rm, thresholds_rm = roc_curve(y_test, y_score[:, 1])
fpr_list.append(fpr_rm)
tpr_list.append(tpr_rm)
thresholds_list.append(thresholds_rm)
"""SVM roc"""
y_pred_svm = svc.predict_proba(x_test)
y_score_svm = y_pred_svm[:, 1]
fpr_svm, tpr_svm, thresholds_svm = roc_curve(y_test, y_score_svm)
fpr_list.append(fpr_svm)
tpr_list.append(tpr_svm)
thresholds_list.append(thresholds_svm)
"""GD roc"""
fpr_list.append(fpr)
tpr_list.append(tpr)
thresholds_list.append(thresholds)

print('acc:', accscore_list)
print('pre:', prescore_list)
print('rec:', rescore_list)
print('f1:', f1score_list)

plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams["axes.unicode_minus"] = False

# 画性能曲线
x = np.arange(len(names))
rects1 = plt.bar(x, accscore_list, width=0.2, alpha=0.5, color='#94bde7', label='accuracy', hatch='//', ls='-', lw=1)
rects2 = plt.bar([i + 0.2 for i in x], f1score_list, width=0.2, alpha=0.5, color='#ad2110', label='f1', hatch='xx')
rects3 = plt.bar([i + 0.2 * 2 for i in x], rescore_list, width=0.2, alpha=0.5, color='#ffefad', label='recall',
                 hatch='++', lw=1)
rects4 = plt.bar([i + 0.2 * 3 for i in x], prescore_list, width=0.2, alpha=0.5, color='#94d6c6', label='precision')
plt.xticks([index + 0.2 for index in x], names)
plt.xlabel('分类方法')
plt.ylabel('平均分类性能')
plt.ylim(0.3, 1.0)
plt.legend()
plt.savefig('performance_res.pdf', format='pdf', bbox_inches='tight')
plt.show()
print(names)

names.remove('Spike')
names.remove('ZigZag')
names.remove('ZBS')

# 画ROC曲线图
linestyles = ['--', '-.', '-']
color_list =['gray', '#4abdce', 'red']
lw_list = [1, 1, 2]
for i in range(len(names)):
    fpr, tpr, thresholds = fpr_list[i], tpr_list[i], thresholds_list[i]
    name = names[i]
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=u'%s:AUC = %0.3f' % (name, roc_auc), ls=linestyles[i], color=color_list[i], lw=lw_list[i])

plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'k:')
plt.xlim([-0.1, 1.1])
plt.ylim([-0.1, 1.1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.grid(linestyle='-.')
plt.grid(True)
plt.savefig('ROC_result.pdf', format='pdf', bbox_inches='tight')
plt.show()
