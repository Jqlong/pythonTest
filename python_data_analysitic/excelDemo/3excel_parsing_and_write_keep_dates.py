from datetime import date
from xlrd2 import open_workbook, xldate_as_tuple
from xlwt import Workbook

"""格式化日期数据"""
input_file = 'sales_2013.xlsx'
output_file = 'output/3_output.xls'
# 创建Workbook对象
output_workbook = Workbook()
# 添加工作表
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 打开文件
with open_workbook(input_file) as workbook:
    # 引用工作表
    worksheet = workbook.sheet_by_name('january_2013')
    # 行索引
    for row_index in range(worksheet.nrows):
        row_list_output = []
        # 列索引
        for col_index in range(worksheet.ncols):
            # 检验单元格类型是否为数字3：包含日期数据
            if worksheet.cell_type(row_index, col_index) == 3:
                # 单独处理
                # cell_value函数作为第一个参数，会被转换成元组中的一个代表日期的浮点数
                # worksheet.datemode是必须的
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)
                print(date_cell)
                # 使用元组索引来引用元组date_cell中的前3个元素(年，月，日)
                # strftime函数将date对象转换为一个具有特定格式的字符串
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                print(date_cell)
                row_list_output.append(date_cell)
                output_worksheet.write(row_index, col_index, date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index, col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index, col_index, non_date_cell)
output_workbook.save(output_file)





