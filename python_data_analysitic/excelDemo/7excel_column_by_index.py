from datetime import date
from xlwt import Workbook
from xlrd2 import open_workbook, xldate_as_tuple
"""选取特定列————列索引值"""
input_file = 'sales_2013.xlsx'
output_file = 'output/7_output.xls'
# 创建对象
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet("jan_2013_output")
my_column = [1, 4]
with open_workbook(input_file) as workbook:
    # 获取工作表
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    # 遍历行
    for row_index in range(worksheet.nrows):
        row_list = []
        # 列遍历
        for column_index in my_column:
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


