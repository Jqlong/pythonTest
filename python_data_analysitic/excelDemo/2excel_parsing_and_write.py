from xlrd2 import open_workbook  # 读
from xlwt import Workbook  # 写
"""读写Excel文件"""
input_file = 'sales_2013.xlsx'
output_file = 'output/2_output.xls'
# 实例化workbook对象，可以将结果写入用于输出的excel文件
output_workbook = Workbook()
# 为输出文件添加一个工作表
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 打开输入文件
with open_workbook(input_file) as workbook:
    # 使用workbook对象引用工作表
    worksheet = workbook.sheet_by_name('january_2013')
    # 循环行
    for row_index in range(worksheet.nrows):
        # 循环列
        for column_index in range(worksheet.ncols):
            # 写
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
# 保存并关闭输出工作簿
output_workbook.save(output_file)

