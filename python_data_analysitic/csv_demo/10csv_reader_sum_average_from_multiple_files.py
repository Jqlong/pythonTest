import csv
import os
import pandas as pd
import glob
"""计算每个文件中值的总和和均值"""

input_path = '../'
output_file = 'supplier_data_test_10.csv'
# 输出文件标的列标题
output_header_list = ['file_name', 'total_sales', 'average_sales']
# 先打开文件
csv_out_file = open(output_file, 'a', newline='', encoding='UTF-8')
# 再创建filewriter对象
filewriter = csv.writer(csv_out_file)
# 最后写入，将标题写入文件中
filewriter.writerow(output_header_list)
# for循环获取输入文件
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    # 打开文件
    with open(input_file, 'r', encoding='UTF-8', newline='') as csv_reader:
        # 再创建filereader对象
        filereader = csv.reader(csv_reader)
        output_list = [ ]
        # 将文件名称存到列表中
        output_list.append(os.path.basename(input_file))
        # 跳过每个文件的标题行-也就是第一行
        header = next(filereader)
        # 定义变量，存储每个文件的总的销售量
        total_sales = 0.0
        # 统计个数，也就是行数，用于计算均值
        number_of_sales = 0.0
        # 一次读取文件的每一行
        for row in filereader:
            # 获取每一行第三列的值，即销售额
            sale_amount = row[3]
            # 去除逗号和💲，转换成float
            total_sales += float(str(sale_amount).strip('$').replace(',', ''))
            number_of_sales += 1
        average_sales = '{0:2f}'.format(total_sales / number_of_sales)
        # 将个数据量追加到列表中
        output_list.append(total_sales)
        output_list.append(average_sales)
        # 将列表写入文件
        filewriter.writerow(output_list)
# 关闭文件
csv_out_file.close()



