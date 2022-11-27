import pandas as pd
"""在所有工作表中筛选特定行"""
input_file = 'sales_2013.xlsx'
output_file = 'output/pandas5_output.xls'
data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)
row_output = []
for worksheet_name, data in data_frame.items():
    # 转换成浮点型
    row_output.append(data[data['Sale Amount'].astype(float) > 1500.0])
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.save()





