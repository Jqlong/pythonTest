import sys
import pandas as pd

input_file = '../supplier_data.csv'
output_file = 'supplier_data_test.csv'
data_frame = pd.read_csv(input_file)
print(data_frame)
print(type(data_frame))
data_frame.to_csv(output_file, index=False)  # 可选mode='a'进行追加

