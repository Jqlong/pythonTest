import pandas as pd
import sys

input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_3.csv'

data_frame = pd.read_csv(input_file)
# 将cost列转换成浮点型
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
condition = data_frame.loc[(data_frame['Supplier Name'].str.contains('Z')) | \
                           (data_frame['Cost'] > 600.0), :]
condition.to_csv(output_file, index=False)
