import pandas as pd
"""筛选特定行————行中的值满足某个条件"""
input_file = 'sales_2013.xlsx'
output_file = 'output/pandas2_output.xls'
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]
writer = pd.ExcelWriter(output_file)
data_frame_value_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()




