"""工作表计数以及每个工作表中的行列计数"""
import glob
import os
from xlrd2 import open_workbook
# 文件夹地址
input_directory = ''
workbook_counter = 0
for input_file in glob.glob(os.path.join(input_directory, '*.xls*')):
    # 打开文件
    workbook = open_workbook(input_file)
    # 输出文件名
    print('Workbook:%s' % os.path.basename(input_file))
    # 输出文件工作表数
    print("Number of worksheets:{0:d}".format(workbook.nsheets))
    # 输出每个表的信息
    for worksheet in workbook.sheets():
        print('Worksheet name:', worksheet.name, '\tRows', worksheet.nrows, '\tColumns:', worksheet.ncols)
    # 文件加一
    workbook_counter += 1
print('Number of Excel workbooks:{0:d}'.format(workbook_counter))






