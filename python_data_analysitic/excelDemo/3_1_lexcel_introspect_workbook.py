
from xlrd2 import open_workbook

"""内省Excel工作簿"""
input_file = 'sales_2013.xlsx'
# 读取和分析excel文件
workbook = open_workbook(input_file)
# 打印工作簿中工作表的数量
print('Number of worksheets:', workbook.nsheets)
# 在工作表之间迭代
for worksheet in workbook.sheets():
    
    print('Worksheet name:', worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)




