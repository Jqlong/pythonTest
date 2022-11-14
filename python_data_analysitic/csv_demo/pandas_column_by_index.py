import pandas as pd
input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_6.csv'

data_frame = pd.read_csv(input_file)
# iloc选取列
# iloc通过行号取数据,index
data_frame_column = data_frame.iloc[:, [0, 2, 4]]
data_frame_column.to_csv(output_file, index=False)

