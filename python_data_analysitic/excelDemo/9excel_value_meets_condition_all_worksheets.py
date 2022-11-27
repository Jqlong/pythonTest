from datetime import date
from xlwt import Workbook
from xlrd2 import open_workbook, xldate_as_tuple
"""在所有工作表中筛选特定行"""
input_file = 'sales_2013.xlsx'
output_file = 'output/9_output.xls'
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('filtered_rows_all_worksheets')
# 保存sale amount列的索引值
sales_column_index = 3
# 条件
threshold = 1500.0
first_worksheet = True
# 打开文件
with open_workbook(input_file) as workbook:
    data = []
    # 循环遍历所有工作表
    for worksheet in workbook.sheets():
        # 判断当前工作表是不是第一个工作表
        if first_worksheet:
            # 如果是，就去出标题行，追加到data中
            header_row = worksheet.row_values(0)
            data.append(header_row)
            # 设置为False
            first_worksheet = False
        # 遍历行
        for row_index in range(1, worksheet.nrows):
            row_list = []
            # 获取sale amount的值
            sale_amount = worksheet.cell_value(row_index, sales_column_index)
            # 进行对比
            if sale_amount > threshold:
                # 如果大，遍历列，写入
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
            if row_list:
                data.append(row_list)
    for list_index, output_list in enumerate(data):
        for element_list, element in enumerate(output_list):
            output_worksheet.write(list_index, element_list, element)
output_workbook.save(output_file)




