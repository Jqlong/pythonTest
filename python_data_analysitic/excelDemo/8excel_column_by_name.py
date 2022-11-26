from datetime import date
from xlwt import Workbook
from xlrd2 import open_workbook, xldate_as_tuple
input_file = 'sales_2013.xlsx'
output_file = 'output/8_output.xls'
output_workbook = Workbook()
# 添加工作表
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 要保存两列的部分
my_column = ['Customer ID', 'Purchase Date']
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    # 标题
    data = [my_column]
    header_list = worksheet.row_values(0)
    header_index_list = []
    # 在列标题之间迭代
    for header_index in range(len(header_list)):
        if header_list[header_index] in my_column:
            header_index_list.append(header_index)
            # 索引值
            print(header_index)
    # 遍历行
    for row_index in range(1, worksheet.nrows):
        row_list = []
        for column_index in header_index_list:
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





