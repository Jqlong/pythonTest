import pandas as pd
"""选取特定列————列标题"""
input_file = 'sales_2013.xlsx'
output_file = 'output/pandas5_output.xls'
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
# iloc通过行号取数据
# loc通过具体值取数据
data_frame_column_by_name = data_frame.loc[:, ['Customer ID', 'Purchase Date']]
writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name='jan_2013_output', index=False)
writer.save()




