import pandas as pd
"""选取特定列————列索引"""
input_file = 'sales_2013.xlsx'
output_file = 'output/pandas4_output.xls'
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
# , [1, 4]表示特定的列保留所有的行
data_frame_column_by_index = data_frame.iloc[:, [1, 4]]
writer = pd.ExcelWriter(output_file)
data_frame_column_by_index.to_excel(writer, sheet_name='jan_2013_output', index=False)
writer.save()



