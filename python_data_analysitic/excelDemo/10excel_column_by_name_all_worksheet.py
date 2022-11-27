"""在所有工作表中选取特定的列"""
from datetime import date
from xlwt import Workbook
from xlrd2 import open_workbook, xldate_as_tuple
input_file = 'sales_2013.xlsx'
output_file = 'output/10_output.xls'
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('selected_columns_all_worksheets')
my_columns = ['Customer Name', 'Sale Amount']
# 定义变量
first_worksheet = True
with open_workbook(input_file) as workbook:
    data = [my_columns]
    # 保存条件列的索引值
    index_of_cols_to_keep = []
    # 遍历工作表
    for worksheet in workbook.sheets():
        # 如果是第一个表
        if first_worksheet:
            header = worksheet.row_values(0)
            for column_index in range(len(header)):
                # 如果在条件列中
                if header[column_index] in my_columns:
                    index_of_cols_to_keep.append(column_index)
            first_worksheet = False
        for row_index in range(1, worksheet.nrows):
            row_list = []
            for column_index in index_of_cols_to_keep:
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








