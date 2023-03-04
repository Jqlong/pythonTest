import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 读取数据
data = pd.read_csv('test_data/all_lose_new.csv',  encoding='gbk')
#
# # 获取特征和标签列
# features = df.iloc[:, :-1]
# label = df.iloc[:, -1]
#
# # 定义空列表用于存储 MAE 值
# mae_list = []
#
# # 定义训练次数
# # num_estimators = [10, 50, 100, 200]
# num_estimators = list(range(1, 200))
#
# # 循环进行多次训练，并计算 MAE 值
# for n in num_estimators:
#     # 初始化随机森林回归器
#     rf = RandomForestRegressor(n_estimators=n, random_state=42)
#     # 进行训练
#     rf.fit(features, label)
#     # 计算训练集 MAE 值
#     train_pred = rf.predict(features)
#     train_mae = mean_absolute_error(label, train_pred)
#     # 计算测试集 MAE 值
#     test_pred = rf.predict(features)
#     test_mae = mean_absolute_error(label, test_pred)
#     # 将训练集和测试集的 MAE 值加入到列表中
#     mae_list.append((train_mae, test_mae))
#     print(n)
#
# # 绘制 MAE 图
# train_mae_list = [x[0] for x in mae_list]
# test_mae_list = [x[1] for x in mae_list]
# plt.plot(num_estimators, train_mae_list, label='Train MAE')
# plt.plot(num_estimators, test_mae_list, label='Test MAE')
# plt.legend()
# plt.xlabel('Number of Estimators')
# plt.ylabel('MAE')
# plt.show()

X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

n_estimators = 100  # 设置树的数量
mae_list = []
for i in range(1, n_estimators):
    rf = RandomForestRegressor(n_estimators=i, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mae_list.append(mae)
    print(i)

plt.plot(range(1, n_estimators), mae_list, label="MAE")
plt.xlabel("Number of trees")
plt.ylabel("MAE")
plt.title("Random Forest MAE with Increasing Trees")
plt.legend()
plt.show()


