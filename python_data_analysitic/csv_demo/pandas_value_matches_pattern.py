import pandas as pd
import re

input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_5.csv'

data_frame = pd.read_csv(input_file)
# loc前面是行，后面是列
data_frame_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith("001-"), :]
data_frame_pattern.to_csv(output_file)


