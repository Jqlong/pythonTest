import pandas as  pd

input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_7.csv'
data_frame = pd.read_csv(input_file)
# loc通过具体值取数据
data_frame_column_byName = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]
data_frame_column_byName.to_csv(output_file, index=False)

