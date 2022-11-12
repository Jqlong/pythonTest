import csv
import sys
input_file = '../supplier_data.csv'
output_file = '/supplier_data_test.csv'
with open(input_file, 'r', newline='', encoding='UTF-8') as csv_reader:
    with open(output_file, 'w', newline='', encoding='UTF-8') as csv_writer:
        filereader = csv.reader(csv_reader, delimiter=',')
        filewriter = csv.writer(csv_writer, delimiter=',')
        for row in filereader:
            # print(row)  # 是个list列表
            print(str(row))
            filewriter.writerow(row)
        print(type(row))

