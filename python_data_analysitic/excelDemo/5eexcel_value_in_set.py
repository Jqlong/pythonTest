from datetime import date
from xlrd2 import open_workbook, xldate_as_tuple
from xlwt import Workbook
"""行中的值属于某个集合"""
input_file = 'sales_2013.xlsx'
output_file = 'output/5_output.xls'
# 创建对象
output_workbook = Workbook()
# 添加工作表
output_sheet = output_workbook.add_sheet('jan_2013_output')
# 条件预设
important_dates = ['01/24/2013', '01/31/2013']
purchase_date_column_index = 4
with open_workbook(input_file) as workbook:
    # 读表
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    # 读取头标题
    header = worksheet.row_values(0)
    # 追加到列表中
    data.append(header)
    # 遍历剩余的列
    for row_index in range(1, worksheet.nrows):
        # 日期
        purchase_datetime = xldate_as_tuple(worksheet.cell_value(row_index, purchase_date_column_index), workbook.datemode)
        # 将日期转换为特定格式
        purchase_date = date(*purchase_datetime[0:3]).strftime('%m/%d/%Y')
        row_list = []
        # 判断日期是否符合条件
        if purchase_date in important_dates:
            # 遍历列
            for column_index in  range(worksheet.ncols):
                # 怎么处理列
                # 获取值
                cell_value = worksheet.cell_value(row_index, column_index)
                # 获取类型
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
            output_sheet.write(list_index, element_index, element)
output_workbook.save(output_file)





