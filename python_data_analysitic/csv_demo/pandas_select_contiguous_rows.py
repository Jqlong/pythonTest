import pandas as pd
import sys
"""选取连续的行"""
input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_11.csv'

data_frame = pd.read_csv(input_file, header=None, sep='\t')

data_frame = data_frame.drop([0, 1, 2, 16, 17, 18])
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3))   # 为数据框重新生成索引

data_frame.to_csv(output_file, index=False)
