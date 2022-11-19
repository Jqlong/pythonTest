import pandas as pd
import os
import glob
import csv

input_path = '../'
output_file = 'supplier_data_test_10.csv'
# 获取所有文件
all_files = glob.glob(os.path.join(input_path, 'sales_*'))
# 创建空的数据框
all_data_frame = []
# 依次读取所有文件
for input_file in all_files:
    # 创建单个文件的数据框
    data_frame = pd.read_csv(input_file, index_col=None)
    # 求总和，销售额的总和 sum()方法求和
    total_cost = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).sum()
    # mean()方法求平均值
    average_cost = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).mean()
    data = {'file_name':os.path.basename(input_file), 'total_sales':total_cost, 'average_sales':average_cost}
    all_data_frame.append(pd.DataFrame(data, columns=['file_name', 'total_sales', 'average_sales']))
# 连接数据框
data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)



