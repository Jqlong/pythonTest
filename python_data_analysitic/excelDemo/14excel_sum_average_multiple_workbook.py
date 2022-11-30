"""为每个工作簿和工作表计算总数和均值"""
from datetime import date
from xlwt import Workbook
from xlrd2 import open_workbook, xldate_as_tuple
import glob
import os
input_path = ''
output_file = 'output/14_output.xls'
output_workbook = Workbook()
# 保存要计算的列的索引值
sales_column_index = 3
output_worksheet = output_workbook.add_sheet('sum_and_average')
# 保存要写入输出文件的所有行
all_data = []
header = ['workbook', 'worksheet', 'worksheet_total', 'worksheet_average', 'workbook_total', 'workbook_average']
all_data.append(header)
for input_file in glob.glob(os.path.join(input_path, '*.xls*')):
    # 依次打开文件
    with open_workbook(input_file) as workbook:
        # 保存工作簿中所有工作表的销售额总和
        list_of_totals = []
        # 保存工作簿的所有工作表中用来计算总销售额的销售额数据个数
        list_of_numbers = []
        # 保存要写入输出文件的所有输出列表 要输出文件名，表名，表的销售总额，表的评价销售总额，文件的销售总额，文件的平均销售额
        workbook_output = []
        # 打开工作表
        for worksheet in workbook.sheets():
            total_sales = 0
            number_of_sales = 0
            # 保存工作表的信息
            worksheet_list = []
            # 添加文件名
            worksheet_list.append(os.path.basename(input_file))
            # 添加工作表名
            worksheet_list.append(worksheet.name)
            for row_index in range(1, worksheet.nrows):
                try:
                    total_sales += float(str(worksheet.cell_value(row_index, sales_column_index)).strip('$').replace(',', ''))
                    number_of_sales += 1
                except:
                    total_sales += 0
                    number_of_sales += 0
            # 计算平均值
            average_sales = '%.2f' % (total_sales / number_of_sales)
            # 添加到
            worksheet_list.append(total_sales)
            worksheet_list.append(float(average_sales))
            list_of_totals.append(total_sales)
            list_of_numbers.append(float(number_of_sales))
            # 保存信息
            workbook_output.append(worksheet_list)
        workbook_total = sum(list_of_totals)
        workbook_average = sum(list_of_totals) / sum(list_of_numbers)
        for list_element in workbook_output:
            list_element.append(workbook_total)
            list_element.append(workbook_average)
        all_data.extend(workbook_output)
for list_index, output_list in enumerate(all_data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)







