import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, classification_report, \
    mean_absolute_error, roc_curve, auc
import pandas as pd
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv('test_data/all_lose_new.csv', encoding='gbk')


X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# rf = RandomForestClassifier(n_estimators=150, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
precision = precision_score(y_test, y_pred, average='macro')
print(classification_report(y_test, y_pred))
print("accuracy", accuracy)
print("f1", f1)
print("recall", recall)
print("precision", precision)

# 性能直方图
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams["axes.unicode_minus"] = False
label_list = ['随机森林', None, None, None]
list1 = [accuracy, 0, 0, 0]
list2 = [f1, 0, 0, 0]
list3 = [recall, 0, 0, 0]
list4 = [precision, 0, 0, 0]
x = range(len(list1))
rects1 = plt.bar(x, height=list1, width=0.2, alpha=0.5, color='red', label='accuracy')
rects2 = plt.bar([i+0.2 for i in x], height=list2, width=0.2, alpha=0.5, color='green', label='f1')
rects3 = plt.bar([i+0.2*2 for i in x], height=list3, width=0.2, alpha=0.5, color='blue', label='recall')
rects4 = plt.bar([i+0.2*3 for i in x], height=list4, width=0.2, alpha=0.5, color='black', label='precision')
plt.xticks([index+0.2 for index in x], label_list)
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

mae_list = []
# num_estimators = [10, 50, 100, 200]
for i in range(1, 200, 10):
    rf1 = RandomForestClassifier(n_estimators=i, random_state=42)
    print(i)
    rf1.fit(X_train, y_train)
    y_pred1 = rf1.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred1)
    mae_list.append(mae)
print(mae_list)
print(min(mae_list))

plt.plot(range(1, 200, 10), mae_list)
plt.show()

# roc曲线
y_score = rf.fit(X_train, y_train).predict_proba(X_test)
fpr, tpr, thresholds = roc_curve(y_test, y_score[:, 1])
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")

plt.legend()

plt.show()







