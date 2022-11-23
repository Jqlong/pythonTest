import sys
from datetime import date
from xlrd2 import open_workbook, xldate_as_tuple
from xlwt import Workbook
"""筛选特定行————行中的值满足某个条件"""
input_file = 'sales_2013.xlsx'
output_file = 'output/4_output.xls'
# 创建Workbook实例
output_workbook = Workbook()
# 添加工作表
output_worksheet = output_workbook.add_sheet('jan_2013_output')
sale_amount_column_index = 3
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    # 创建空列表
    data = []
    # 提取标题的值
    header = worksheet.row_values(0)
    # 追加到data中
    data.append(header)
    # 行索引
    for row_index in range(1, worksheet.nrows):
        row_list = []
        # 保存行中的销售额
        sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)
        print(sale_amount)
        print(type(sale_amount))
        # 处理销售额大于1400的行
        if sale_amount > 1400.0:
            # 处理每个单元格的值 列
            for column_index in range(worksheet.ncols):
                # 把值赋给cell_value
                cell_value = worksheet.cell_value(row_index, column_index)
                # 获取类型
                cell_type = worksheet.cell_type(row_index, column_index)
                # 检验是否是日期类型
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        # 为每一行都创建list，判断非空，加入data中
        if row_list:
            data.append(row_list)
    # 保证行与行不出现缺口
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)




