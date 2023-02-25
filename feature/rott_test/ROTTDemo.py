import pandas as pd
from decimal import Decimal
from xlrd import open_workbook
import numpy as np
input_file = '../test_data.xls'
data_frame = pd.read_excel(input_file)
# 第三列特征，用于选择是否为零
feature_num = 2
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('Sheet1')
    # 循环行 行数
    ROTT_result = []
    count = 0
    for row_index in range(1, worksheet.nrows):
        # print(worksheet.cell_value(row_index))
        feature_amount = int(worksheet.cell_value(row_index, feature_num))
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
        else:
            # 字符串类型
            # print(ROTT_result)
            # 把ROTT_result写入文件
            data = pd.DataFrame(ROTT_result)
            print(data)
            data_frame.loc[row_index-len(data), 'ROTT'] = data
            # data_frame['ROTT'] = data
            data_frame.to_excel('output/result.xls', index=None)
            count += 1
            if ROTT_result:
                # ROTT_min
                ROTT_min = np.min(ROTT_result)
                print('ROTT_min:', ROTT_min)
                data_frame.loc[row_index - 2, 'ROTT_min'] = ROTT_min


                # ROTT_mean
                ROTT_mean = np.mean(ROTT_result)  # numpy.float64
                print('ROTT_mean', round(ROTT_mean.astype(float), 6))  # numpy.float64

                # ROTT_dev
                ROTT_dev = ROTT_result - round(ROTT_mean, 5)
                # ROTT_dev = ROTT_result - ROTT_mean
                print('ROTT_dev', ROTT_dev)
                data_dev = pd.DataFrame(ROTT_dev)
                data_frame['ROTT_dev'] = data_dev
                data_frame.to_excel('output/result.xls', index=None)

                # ROTT/ROTT_mean
                ROTT_ROTT_mean = ROTT_result / round(ROTT_mean, 5)
                print('ROTT_ROTT_mean', ROTT_ROTT_mean)

                # ROTT_ROTT_max
                ROTT_ROTT_max = ROTT_result / np.max(ROTT_result)
                print('ROTT_ROTT_max', ROTT_ROTT_max)

                # ROTT_ROTT_min
                ROTT_ROTT_min = ROTT_result / ROTT_min
                print('ROTT_ROTT_min', ROTT_ROTT_min)

                # ROTT_ROTT_min_mean
                ROTT_ROTT_min_mean = ROTT_min / ROTT_mean
                print('ROTT_ROTT_min_mean', ROTT_ROTT_min_mean)
                data_frame.loc[row_index - 2, 'ROTT_min_mean'] = ROTT_ROTT_min_mean

                # ROTT_ROTT_mean_dev
                ROTT_ROTT_mean_dev = ROTT_result / (ROTT_mean - ROTT_dev)
                print('ROTT_ROTT_mean_dev', ROTT_ROTT_mean_dev)

                # ROTT_ROTT_mean_dev2
                ROTT_ROTT_mean_dev2 = ROTT_result / (ROTT_mean - ROTT_dev / 2)
                print('ROTT_ROTT_mean_dev2', ROTT_ROTT_mean_dev2)
            # else:
            #     count += 1
            # 统计获得的rott最小值
            print('count', count)
            print(row_index)
            print('------')
            count = 0
            ROTT_result = []
        # 判断列表是否为空

data_frame.to_excel('output/result.xls', index=None)

