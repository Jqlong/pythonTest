import pandas as pd
from decimal import Decimal
from xlrd import open_workbook
import numpy as np

# 比较完整的

input_file = '../test_data.xls'
data_frame = pd.read_excel(input_file)
# 第三列特征，用于选择是否为零
feature_num = 2


def data_result(rott_list, row_index):  # 计算值
    rott = pd.DataFrame(rott_list)  # 这是DataFrame格式     列表
    # 写rott
    for i in range(0, len(rott)):  # 从零开始
        data_frame.at[row_index - len(rott) - 1 + i, 'ROTT'] = rott_list[i]

    rott_min = np.min(rott_list)    # 数字
    # 写rott_min
    data_frame.loc[row_index - 2, 'ROTT_min'] = rott_min

    rott_mean = np.mean(rott_list)    # 数字
    # 写rott_mean
    data_frame.loc[row_index - 2, 'ROTT_mean'] = round(rott_mean, 6)

    ROTT_dev_Data = rott_list - rott_mean    # 列表
    rott_dev = pd.DataFrame(ROTT_dev_Data)   # DataFrame格式
    # 写rott_dev
    for i in range(0, len(rott)):  # 从零开始
        data_frame.at[row_index - len(rott) - 1 + i, 'ROTT_dev'] = round(ROTT_dev_Data[i], 6)

    ROTT_ROTT_mean_Data = rott_list / rott_mean    # 列表
    rott_rott_mean = pd.DataFrame(ROTT_ROTT_mean_Data)  # DataFrame格式
    # 写rott_rott_mean
    for i in range(0, len(rott)):  # 从零开始
        data_frame.at[row_index - len(rott) - 1 + i, 'ROTT_ROTT_mean'] = round(ROTT_ROTT_mean_Data[i], 6)

    ROTT_ROTT_max_Data = rott_list / np.max(rott_list)    # 列表
    rott_rott_max = pd.DataFrame(ROTT_ROTT_max_Data)  # DataFrame格式
    # 写rott_rott_max
    for i in range(0, len(rott)):  # 从零开始
        data_frame.at[row_index - len(rott) - 1 + i, 'ROTT_ROTT_max'] = round(ROTT_ROTT_max_Data[i], 6)

    ROTT_ROTT_min_Data = rott_list / rott_min    # 列表
    rott_rott_min = pd.DataFrame(ROTT_ROTT_min_Data)  # DataFrame格式
    # 写rott_rott_min
    for i in range(0, len(rott)):  # 从零开始
        data_frame.at[row_index - len(rott) - 1 + i, 'ROTT_ROTT_min'] = round(ROTT_ROTT_min_Data[i], 6)

    rott_min_mean =rott_min / rott_mean    # 数字
    # 写rott_min_mean
    data_frame.loc[row_index - 2, 'ROTT_min_mean'] = rott_min_mean

    ROTT_ROTT_mean_dev_Data = rott_list / (rott_mean - ROTT_dev_Data)    # 列表
    rott_rott_mean_dev = pd.DataFrame(ROTT_ROTT_mean_dev_Data)
    # 写rott_rott_mean_dev
    for i in range(0, len(rott)):  # 从零开始
        data_frame.at[row_index - len(rott) - 1 + i, 'ROTT_ROTT_mean_dev'] = round(ROTT_ROTT_mean_dev_Data[i], 6)

    ROTT_ROTT_mean_dev_2_Data = rott_list / (rott_mean - ROTT_dev_Data / 2)    # 列表
    rott_rott_mean_dev_2 = pd.DataFrame(ROTT_ROTT_mean_dev_2_Data)
    # 写rott_rott_mean_dev_2
    for i in range(0, len(rott)):  # 从零开始
        data_frame.at[row_index - len(rott) - 1 + i, 'ROTT_ROTT_mean_dev2'] = round(ROTT_ROTT_mean_dev_2_Data[i],
                                                                                    6)


with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('Sheet1')
    # 循环行 行数
    ROTT_result = []
    count = 0
    for row_index in range(1, worksheet.nrows):  # 遍历行
        # print(worksheet.cell_value(row_index))
        feature_amount = int(worksheet.cell_value(row_index, feature_num))  # 第三列的值
        # 如果为零 计算相关量
        if feature_amount == 0:
            num1 = worksheet.cell_value(row_index, 1)
            result1 = float(num1)
            num2 = worksheet.cell_value(row_index, 0)
            result2 = float(num2)
            result = float(format(result1 - result2, '.6f'))
            # 获得ROTT
            ROTT_result.append(result)
        # 遇到丢包
        else:  # 丢包
            # 字符串类型
            if ROTT_result:
                print()
                data_result(ROTT_result, row_index)
            print('count', count)
            print(row_index)
            print('------')
            count = 0
            ROTT_result = []
        # 判断列表是否为空
        if row_index == worksheet.nrows - 1:  # 最后一行
            data_result(ROTT_result, row_index + 1)

data_frame.to_excel('output/result.xls', index=None)
