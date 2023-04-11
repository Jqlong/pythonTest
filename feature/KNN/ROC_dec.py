import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, classification_report

# 生成具有相关性的二分类数据
X, y = make_classification(n_samples=5000, n_features=5, n_informative=3,
                           n_redundant=0, n_clusters_per_class=1, random_state=42)
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X, y, random_state=42, test_size=0.3)

# 使用逻辑回归模型训练并生成预测概率
lr = LogisticRegression(random_state=42)
lr.fit(X, y)

# y_prep = lr.predict(X_test_1)
# accuracy = accuracy_score(y_test_1, y_prep)
# f1 = f1_score(y_test, y_prep, average='macro')
# recall = recall_score(y_test, y_prep, average='macro')
# precision = precision_score(y_test, y_prep, average='macro')

# print(classification_report(y_test, y_prep))
# print("accuracy", accuracy)
# print("f1", f1)
# print("recall", recall)
# print("precision", precision)

y_prob = lr.predict_proba(X)[:, 1]

# 计算ROC曲线和AUC
fpr, tpr, thresholds = roc_curve(y, y_prob)
roc_auc = auc(fpr, tpr)
# print(fpr)
# data = pd.DataFrame([fpr, tpr, thresholds])
# data.to_csv('roc_fpr_tpr.csv')
# print(type(fpr))
# print(tpr)
# print(type(tpr))
# print(thresholds)

# 绘制ROC曲线
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()
