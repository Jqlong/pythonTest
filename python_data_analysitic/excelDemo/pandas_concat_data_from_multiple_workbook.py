"""从多个工作簿中连接数据"""
import glob
import os
import pandas as pd
input_path = ''
output_file = 'output/pandas6_output.xls'
all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))
data_frame = []
for workbook in all_workbooks:
    # 读文件工作表
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    for worksheet_name, data in all_worksheets.items():
        # 添加数据
        data_frame.append(data)
all_data_concatenated = pd.concat(data_frame, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
writer.save()








