import pandas as pd
"""pandas读写excel文件"""
input_file = 'sales_2013.xlsx'
output_file = 'output/pandas_output.xls'

data_frame = pd.read_excel(input_file, sheet_name='january_2013')
writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()


