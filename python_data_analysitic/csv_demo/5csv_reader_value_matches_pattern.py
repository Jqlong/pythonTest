import csv
import re  # 正则表达式模块

input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_5.csv'
# 正则表达式  表示已001开头就行
# . 表示可以匹配任何字符，除了换行符
# * 表示重复前面的字符0次或任意次
pattern = re.compile(r'(?P<my_pattern_group>001-.*)', re.I)
with open(input_file, 'r', newline='', encoding='UTF-8') as csv_reader:
    with open(output_file, 'w', newline='', encoding='UTF-8') as csv_writer:
        filereader = csv.reader(csv_reader)
        filewriter = csv.writer(csv_writer)
        header = next(filereader)
        filewriter.writerow(header)
        for row in filereader:
            invoice = row[1]
            if pattern.search(invoice):
                filewriter.writerow(row)


