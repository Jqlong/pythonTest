import csv
import glob
import os
"""从多个文件中链接数据"""

input_path = '../'
output_file = 'supplier_data_test_9.csv'
# 用于保证标题只输出一次
first_file = True
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_path))  # 输出文件名称
    with open(input_file, 'r', newline='', encoding='UTF-8') as csv_reader:
        with open(output_file, 'a', newline='', encoding='UTF-8') as csv_writer:

            filereader = csv.reader(csv_reader)
            filewriter = csv.writer(csv_writer)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                header = next(filereader, None)
                for row in filereader:
                    filewriter.writerow(row)



