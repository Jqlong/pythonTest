import pandas as pd
import glob
import os

input_path = '../'
output_file = 'supplier_data_test_12.csv'
all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frame = []  # 空的数据框
for file in all_files:  # 遍历数据
    # 为每一个文件创建一个数据框  重新设置一列为index值
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frame.append(data_frame)  # 追加到数据框

# 设置链接数据框的方式
data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)


