import pandas as pd

input_file = 'test_data.xls'
data_frame = pd.read_excel(input_file)
print(data_frame)
print(data_frame.drop(index=[10]))

data_frame.drop(index=[10]).to_excel('output/drop_test.xls', index=None)


