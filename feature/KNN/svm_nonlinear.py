import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report, roc_auc_score, roc_curve, auc, accuracy_score, precision_score, \
    recall_score, f1_score
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV

# 消除警告
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)

data = pd.read_csv("../relief/all_lose_new.csv", encoding='gbk')
target = data["丢包类别"]
data = pd.DataFrame(data, columns=['IATmean', 'ROTT', 'ROTT_min_mean', 'IATmax', '临近IAT比值', 'ROTT_ROTT_min',
                                   'ROTT_dev', 'Numloss', 'ROTT_ROTT_mean_dev', 'ROTT_ROTT_mean'])

# 用非线性支持向量机svm.SVC去拟合，并查看拟合模型在训练集上的精度
"""
第一行，我们默认使用高斯函数作为核函数，所以我们需要定义σ^2参数，代码中用gamma表示，这里我们定为10，这个σ^2
参数会影响我们的拟合情况，具体地说：太大的σ^2会使高斯函数过于平坦，而导致高偏差、低方差：反之，还会导致高方差，低偏差。
所以惩戒参数数C和参数σ^2的选取都极为重要。
probability表示是否用概率估计，此参数定义一定要在调用fit之后，设置为False之后会使训练过程的计算过程变慢。
"""
# svc = svm.SVC(C=100,gamma=10,probability=True)
svc = svm.SVC(probability=True, C=1000, gamma=0.4, kernel='rbf')
# svc = svm.SVC(probability=True)
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=1)
# #自带参数得分为:Accuracy: 0.81 (+/- 0.04)
# #调过参数后得分为:Accuracy: 0.84 (+/- 0.03)
# scores = cross_val_score(svc, x_train,y_train, cv=10)
# print(scores)
# print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

# #网格搜索调参：
# # param_grid = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4, 0.1, 0.2, 0.3,0.4],
# #                         'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]},
# #                     {'kernel': ['linear'], 'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}]
# param_grid = {'kernel': ['rbf'], 'gamma': [ 0.3,0.4,0.5,0.6,1,10],
#                         'C': [ 1, 10, 100, 1000,2000,10000]}      #[1e-3, 1e-4, 0.1, 0.2, 0.3,0.4]-0.4   [0.001, 0.01, 0.1, 1, 10, 100, 1000]1000
# gs = GridSearchCV(estimator=svc,
#                 param_grid = param_grid,
#                 scoring = 'accuracy',
#                 cv = 10,
#                 n_jobs=3)       # 10折交叉验证
# gs = gs.fit(data,target)
# print("网格搜索最优得分：",gs.best_score_)
# print("网格搜索最优参数组合：\n",gs.best_params_)
# #网格搜索最优得分： 0.8315751171658954
# # 网格搜索最优参数组合：
# #  'C': 1000, 'gamma': 0.4, 'kernel': 'rbf'


svc.fit(x_train, y_train)  # 放入训练数据进行训练
pre_result = svc.predict(x_test)  # 测试集预测结果
sore = svc.score(x_test, y_test)
print("预测准确率：", sore)
# 精确率(Precision)与召回率(Recall)
report = classification_report(y_test, pre_result, target_names=["拥塞丢包", "误码丢包"])
print(report)

# 画roc曲线
predict_probs = svc.predict_proba(x_test)
y_score = predict_probs[:, 1]
# print(y_test,y_score)
fpr, tpr, thresholds = roc_curve(y_test, y_score)
roc_auc = auc(fpr, tpr)
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, '#9400D3', label=u'AUC = %0.3f' % roc_auc)

plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([-0.1, 1.1])
plt.ylim([-0.1, 1.1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.grid(linestyle='-.')
plt.grid(True)
plt.show()
print(roc_auc)
#
