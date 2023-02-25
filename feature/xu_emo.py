import os
import pandas as pd
import numpy as np

os.chdir("./data")
df1 = pd.read_excel("数据包丢失原因区分仿真.xls")


# print(df1)

def other_iat(a, list):  # 计算由iat各种运算得到的数据
    iatmin = min(list)
    iatmax = max(list)
    iatmean = np.mean(list, axis=0)
    # print(a)
    i1imean = a / iatmean[0]  # iat / iatmean
    i1imin = a / iatmin[0]  # iat / iatmin
    i1imax = a / iatmax[0]  # iat / iatmax
    imin1imean = iatmin[0] / iatmean[0]  # iatmin / iatmean
    # print(iatmin[0], iatmax[0], iatmean[0], i1imin, i1imax, i1imean, imin1imean)
    return iatmin[0], iatmax[0], iatmean[0], i1imin, i1imax, i1imean, imin1imean


list1 = []  # [[到达时间,包处理类型]]二维数组
list2 = []  # 丢包位置(第几个包丢失)
iat_list = []  # IAT值
alliat_list = []  # 通过IAT计算得到的值[iat，iatmin，iatmax，iatmean，丢包位置](初始包认为丢包位置为-1)
j = -1

for i in df1.index.values:  # 将df数据转为列表型数据
    row_data = df1.loc[i, ['到达时间', '包处理类型：0入队，1误码，2拥塞']].to_list()
    list1.append(row_data)
# print(len(list1))
for i in range(len(list1)):  # 取丢包位置
    if list1[i][1] != 0:  # range(0,10)范围是0到9
        list2.append(i)
# print(list2)
# print(len(list1))
for i in list2:  # 计算iat值，最后一次丢包到最后没有计算
    if i - j > 2:
        for k in range(j + 1, i - 1):
            iat = list1[k + 1][0] - list1[k][0]
            iat_list.append([iat, j])
    j = i
for i in range(list2[-1] + 1, len(list1) - 1):  # 计算iat值，最后一次丢包到最后的
    iat = list1[i + 1][0] - list1[i][0]
    iat_list.append([iat, list2[-1]])
# print(iat_list)
list2.append(-1)
list2.sort()
j = 0
for i in list2:  # 求的iatmin max mean
    for k in range(j, len(iat_list)):
        if iat_list[k][1] == i:
            iatmin, iatmax, iatmean, i1imin, i1imax, i1imean, imin1imean = other_iat(iat_list[k][0], iat_list[j:k + 1])
            alliat_list.append(
                [iat_list[k][0], iatmin, iatmax, iatmean, i1imin, i1imax, i1imean, imin1imean, iat_list[k][1]])
        else:
            j = k
            break
print(alliat_list)
