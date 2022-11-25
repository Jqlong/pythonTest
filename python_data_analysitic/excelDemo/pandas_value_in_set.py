import pandas as pd
"""行中的值属于某个集合"""
input_file = 'sales_2013.xlsx'
output_file = 'output/pandas2_output.xls'
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
important_dates = ['01/24/2013', '01/31/2013']
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dates)]
writer = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()



