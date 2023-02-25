import pandas as pd
from decimal import Decimal
from xlrd import open_workbook
import numpy as np

# 比较完整的
# 新增  间隔丢包算成连续丢包，将其改为-1
# 新增  丢包个数
# 新增  提取丢包行

input_file = '../test_data/everypkt%5.xls'
# input_file = 'test_data.xls'
data_frame = pd.read_excel(input_file)
# 第三列特征，用于选择是否为零
feature_num = 2

# 写文件
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
    worksheet = workbook.sheet_by_name('sheet1')
    # 循环行 行数
    ROTT_result = []
    count = 0
    list_len_1 = 0
    flag = True
    for row_index in range(1, worksheet.nrows):  # 遍历行
        # print(worksheet.cell_value(row_index))
        feature_amount = int(worksheet.cell_value(row_index, feature_num))  # 第三列的值
        # 如果为零 计算相关量
        if feature_amount == 0:
            # 设置flag
            flag = True
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
            # 遇到丢包 count+1，同时flag=False
            flag = False
            count += 1
            if len(ROTT_result) > 1:  # 对间隔接受的包当成连续丢包
                print()
                data_result(ROTT_result, row_index)
            if len(ROTT_result) == 1:  # 如果为1  不处理
                # 将第三列的值改为-1
                # data_frame.at[row_index - 2, '包处理类型：0入队，1误码，2拥塞'] = -1
                # feature_amount = -1
                # 同时丢包个数加一
                # count += 1
                # count = 0
                # list_len_1 += 1
                flag = False

                ROTT_result = []
                continue   # 结束本次循环

            # print('count', count)
            print(row_index)
            print('------')
            # count = 0
            ROTT_result = []
        # 判断列表是否为空
        if row_index == worksheet.nrows - 1:  # 最后一行
            data_result(ROTT_result, row_index + 1)
        if flag:
            if count >= 1:
                print('count', count)
                # 将丢包个数写入文件中
                # data_frame.loc[row_index - 1 - count, 'NUM_lose'] = count + list_len_1
                data_frame.loc[row_index - 1 - count - (list_len_1 * 2), 'NUM_lose'] = count + list_len_1

                data_frame.at[row_index - 1 - count, 'ROTT'] = data_frame.at[row_index - count - 2, 'ROTT']
                data_frame.at[row_index - 1 - count, 'ROTT_min'] = data_frame.at[row_index - count - 2, 'ROTT_min']
                data_frame.at[row_index - 1 - count, 'ROTT_mean'] = data_frame.at[row_index - count - 2, 'ROTT_mean']
                data_frame.at[row_index - 1 - count, 'ROTT_dev'] = data_frame.at[row_index - 2 - count, 'ROTT_dev']
                data_frame.at[row_index - 1 - count, 'ROTT_ROTT_mean'] = data_frame.at[row_index - 2 - count, 'ROTT_ROTT_mean']
                data_frame.at[row_index - 1 - count, 'ROTT_ROTT_max'] = data_frame.at[row_index - count - 2, 'ROTT_ROTT_max']
                data_frame.at[row_index - 1 - count, 'ROTT_ROTT_min'] = data_frame.at[row_index - count - 2, 'ROTT_ROTT_min']
                data_frame.at[row_index - 1 - count, 'ROTT_min_mean'] = data_frame.at[row_index - count - 2, 'ROTT_min_mean']
                data_frame.at[row_index - 1 - count, 'ROTT_ROTT_mean_dev'] = data_frame.at[row_index - count - 2, 'ROTT_ROTT_mean_dev']
                data_frame.at[row_index - 1 - count, 'ROTT_ROTT_mean_dev2'] = data_frame.at[row_index - 2 - count, 'ROTT_ROTT_mean_dev2']
            count = 0  # n清零
            # list_len_1 = 0


data_frame.to_excel('output/result_lose_1.xls', index=None)
# data_frame.to_excel('output/result.xls', index=None)


# 提取丢包行
all_data_file = '../output/result_lose_1.xls'
# all_data_file = 'output/result.xls'
#
data_frame_lose = pd.read_excel(all_data_file)
# feature_num = 2
lose_data = data_frame_lose.loc[data_frame_lose['NUM_lose'].notnull()]
lose_data.to_excel('output/every1_lose.xls', index=False)
# lose_data.to_excel('output/drop_test.xls', index=False)

# 加起来
file = '../output/every1_lose.xls'
# file = 'output/drop_test.xls'
final_data_frame = pd.read_excel(file)

with open_workbook(file) as workbook:
    worksheet = workbook.sheet_by_name('Sheet1')

    count = 0
    num_sum = 0
    cc_flag = True
    for row_index in range(1, worksheet.nrows):
        # 统计第四列为空的个数，并加到前面
        num = int(worksheet.cell_value(row_index, 13))
        cell = worksheet.cell(row_index, 3)
        if cell.ctype == 0:  # 为空
            cc_flag = False
            count += 1
            num_sum += num
            if row_index == worksheet.nrows - 1:  # 为最后一列，直接加上去
                final_data_frame.loc[row_index - count - 1, 'NUM_lose'] = num_sum + int(
                    worksheet.cell_value(row_index - count - 2, 13))
                break
            else:
                continue
        else:  # 不为空
            cc_flag = True
            # if row_index == worksheet.nrows - 1:

        if cc_flag:
            if count >= 1:
                # 写
                final_data_frame.loc[row_index - count - 2, 'NUM_lose'] = num_sum + int(worksheet.cell_value(row_index - count - 2, 13))
        count = 0
        num_sum = 0
final_data_frame_true = final_data_frame.loc[final_data_frame['ROTT'].notnull()]
# final_data_frame.to_excel('output/final_lose.xls', index=None)
final_data_frame_true.to_excel('output/final_lose_ture5.xls', index=None)





