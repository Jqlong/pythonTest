import pandas as pd

input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_4.csv'
data_frame = pd.read_csv(input_file)
condition = ['1/20/14', '1/30/14']
# isin是否在里面
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(condition), :]
data_frame_value_in_set.to_csv(output_file, index=False)
