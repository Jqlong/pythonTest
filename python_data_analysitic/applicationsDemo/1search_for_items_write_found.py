""""在一个大文件集合中查找一组项目"""
import glob
import os
import csv
from datetime import date
from xlrd2 import open_workbook, xldate_as_tuple
# 要搜索的数值项目的csv文件的路径名
item_numbers_file = 'item_numbers_to_find.csv'
# 包含要搜索的文件的文件夹路径
path_to_folder = 'file_archive/'
# 输出文件
output_file = 'output/1app_output.csv'
# 要搜索的数值项目，设为一个空列表
item_numbers_to_find = []
# 读文件
with open(item_numbers_file, 'r', newline='') as item_numbers_csv_file:
    filereader = csv.reader(item_numbers_csv_file)
    for row in filereader:
        item_numbers_to_find.append(row[0])
print(item_numbers_to_find)
# 打开输出文件，创建对象
filewriter = csv.writer(open(output_file, 'a', newline=''))
# 文件数量
file_counter = 0
# 输入文件和工作表中读出的行数
line_counter = 0
# 搜索的数值项目的行数
count_of_item_numbers = 0
# 读取文件夹中所有的文件
for input_file in glob.glob(os.path.join(path_to_folder, '*.*')):
    # 文件数量加一
    file_counter += 1
    # 如果文件是csv格式
    if input_file.split('.')[1] == 'csv':
        # 打开文件
        with open(input_file, 'r', newline='') as csv_in_file:
            # 创建对象
            filereader = csv.reader(csv_in_file)
            # 读取标题
            header = next(filereader)
            # 遍历行
            for row in filereader:
                # 输出列表
                row_of_output = []
                # 遍历列
                for column in range(len(header)):
                    # 如果是第四列，销售额
                    if column == 3:
                        # 去掉左边的$，转换成字符串后去掉首位空格等格式
                        cell_value = str(row[column]).lstrip("$").replace(',', '').strip()
                        # 追加到输出列表中
                        row_of_output.append(cell_value)
                    else:
                        # 否则
                        # 直接转换成字符串
                        cell_value = str(row[column]).strip()
                        # 追加到输出列表中
                        row_of_output.append(cell_value)
                # 将文件名追加到输出列表中，只保存文件名，不保存路径
                row_of_output.append(os.path.basename(input_file))
                # 如果该行的第一列的值是目标值
                if row[0] in item_numbers_to_find:
                    # 将其写入输出文件中
                    filewriter.writerow(row_of_output)
                    # 目标行数加一
                    count_of_item_numbers += 1
                # 总行数加一
                line_counter += 1
    # 处理xls和xlsx文件
    elif input_file.split('.')[1] == 'xls' or input_file.split('.')[1] == 'xlsx':
        # 打开文件
        workbook = open_workbook(input_file)
        # 每个文件的工作表循环
        for worksheet in workbook.sheets():
            try:
                # 读取每个表的标题行
                header = worksheet.row_values(0)
            except IndexError:
                pass
            # 从第二行开始遍历
            for row in range(1, worksheet.nrows):
                # 输出列表
                row_of_output = []
                # 遍历列
                for column in range(len(header)):
                    # 如果列的类型是3类，日期类
                    if worksheet.cell_type(row, column) == 3:
                        # 处理日期
                        cell_value = xldate_as_tuple(worksheet.cell(row, column).value, workbook.datemode)
                        cell_value = str(date(*cell_value[0:3])).strip()
                        row_of_output.append(cell_value)
                    else:
                        cell_value = str(worksheet.cell_value(row, column)).strip()
                        row_of_output.append(cell_value)
                # 追加文件名
                row_of_output.append(os.path.basename(input_file))
                # 追加工作表名
                row_of_output.append(worksheet.name)
                #
                if str(worksheet.cell(row, 0).value).split('.')[0].strip() in item_numbers_to_find:
                    filewriter.writerow(row_of_output)
                    count_of_item_numbers += 1
                line_counter += 1
print('Number of files:', file_counter)
print('Number of lines:', line_counter)
print('Number of item numbers:', count_of_item_numbers)







