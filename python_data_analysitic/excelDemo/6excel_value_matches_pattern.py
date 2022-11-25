import re
from datetime import date
from xlrd2 import xldate_as_tuple, open_workbook
from xlwt import Workbook
"""行中的值匹配于特定模式"""
input_file = 'sales_2013.xlsx'
output_file = 'output/6_output.xls'
# 创建对象
output_workbook = Workbook()
# 添加工作表
output_worksheet = output_workbook.add_sheet('jan_2013_output')
pattern = re.compile(r'(?P<my_pattern>^J.*)')
customer_name_column_index = 1
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    # 获取行
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1, worksheet.nrows):
        row_list = []
        # 如果模式匹配，就遍历列
        if pattern.search(worksheet.cell_value(row_index, customer_name_column_index)):
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)




