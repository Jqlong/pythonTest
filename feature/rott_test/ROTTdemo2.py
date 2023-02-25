import pandas as pd
from decimal import Decimal
from xlrd import open_workbook
import numpy as np

input_file = '../数据包丢失原因区分仿真.xls'
data_frame = pd.read_excel(input_file)
# 第三列特征，用于选择是否为零
feature_num = 2




with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('sheet1')
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
            # result = float('{0:.6f}'.format(result1 - result2))
            # 获得ROTT
            ROTT_result.append(result)
        # 遇到丢包
        else:  # 丢包
            # 字符串类型
            if ROTT_result:
                # 把ROTT_result写入文件
                data = pd.DataFrame(ROTT_result)
                print(data)
                # print(len(data))

                for i in range(0, len(data)):  # 从零开始
                    data_frame.at[row_index - len(data) - 1 + i, 'ROTT'] = ROTT_result[i]

                # ROTT_min
                ROTT_min = np.min(ROTT_result)
                # print('ROTT_min:', ROTT_min)
                data_frame.loc[row_index - 2, 'ROTT_min'] = ROTT_min

                # ROTT_mean
                ROTT_mean = np.mean(ROTT_result)  # numpy.float64
                data_frame.loc[row_index - 2, 'ROTT_mean'] = round(ROTT_mean, 6)

                # ROTT_dev
                ROTT_dev = ROTT_result - ROTT_mean
                data_dev = pd.DataFrame(ROTT_dev)
                for i in range(0, len(data)):  # 从零开始
                    data_frame.at[row_index - len(data) - 1 + i, 'ROTT_dev'] = round(ROTT_dev[i], 6)

                # ROTT/ROTT_mean
                ROTT_ROTT_mean = ROTT_result / ROTT_mean
                data_rott_mean = pd.DataFrame(ROTT_ROTT_mean)
                for i in range(0, len(data)):  # 从零开始
                    data_frame.at[row_index - len(data) - 1 + i, 'ROTT_ROTT_mean'] = round(ROTT_ROTT_mean[i], 6)

                # ROTT/ROTT_max
                # ROTT_ROTT_max
                ROTT_ROTT_max = ROTT_result / np.max(ROTT_result)
                data_rott_max = pd.DataFrame(ROTT_ROTT_max)
                for i in range(0, len(data)):  # 从零开始
                    data_frame.at[row_index - len(data) - 1 + i, 'ROTT_ROTT_max'] = round(ROTT_ROTT_max[i], 6)

                # ROTT_ROTT_min
                ROTT_ROTT_min = ROTT_result / ROTT_min
                data_rott_min = pd.DataFrame(ROTT_ROTT_min)
                for i in range(0, len(data)):  # 从零开始
                    data_frame.at[row_index - len(data) - 1 + i, 'ROTT_ROTT_min'] = round(ROTT_ROTT_min[i], 6)

                # ROTT_ROTT_min_mean
                ROTT_ROTT_min_mean = ROTT_min / ROTT_mean
                data_frame.loc[row_index - 2, 'ROTT_min_mean'] = ROTT_ROTT_min_mean

                # ROTT_ROTT_mean_dev
                ROTT_ROTT_mean_dev = ROTT_result / (ROTT_mean - ROTT_dev)
                data_rott_mean_dev = pd.DataFrame(ROTT_ROTT_mean_dev)
                for i in range(0, len(data)):  # 从零开始
                    data_frame.at[row_index - len(data) - 1 + i, 'ROTT_ROTT_mean_dev'] = round(ROTT_ROTT_mean_dev[i], 6)

                # ROTT_ROTT_mean_dev2
                ROTT_ROTT_mean_dev2 = ROTT_result / (ROTT_mean - ROTT_dev / 2)
                data_rott_mean_dev2 = pd.DataFrame(ROTT_ROTT_mean_dev2)
                for i in range(0, len(data)):  # 从零开始
                    data_frame.at[row_index - len(data) - 1 + i, 'ROTT_ROTT_mean_dev2'] = round(ROTT_ROTT_mean_dev2[i],
                                                                                                6)
            # else:
            #     count += 1
            # 统计获得的rott最小值
            print('count', count)
            print(row_index)
            print('------')
            count = 0
            ROTT_result = []
        # 判断列表是否为空
        if row_index == worksheet.nrows - 1:  # 最后一行
            print('guigiubiubui')
            print(ROTT_result)

data_frame.to_excel('output/result2.xls', index=None)
