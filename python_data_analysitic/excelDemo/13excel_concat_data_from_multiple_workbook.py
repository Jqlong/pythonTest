"""从多个工作簿中连接数据"""
import glob
import os
from datetime import date
from xlrd2 import open_workbook,xldate_as_tuple
from xlwt import Workbook
input_path = ''
output_file = 'output/13_output.xls'
# 创建对象
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('all_data_all_workbooks')
data = []
first_worksheet = True
# 遍历所有文件
for input_file in glob.glob(os.path.join(input_path, '*.xls*')):
    # 输出文件名字
    print(os.path.basename(input_file))
    # 打开文件
    with open_workbook(input_file) as workbook:
        for worksheet in workbook.sheets():
            if first_worksheet:
                header_row = worksheet.row_values(0)
                data.append(header_row)
                first_worksheet = False
            # 遍历行
            for row_index in range(1, worksheet.nrows):
                row_list = []
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
                data.append(row_list)
for list_index, output_list in enumerate(data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)









