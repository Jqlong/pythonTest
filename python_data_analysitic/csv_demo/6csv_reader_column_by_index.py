import csv
import sys
input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_6.csv'

# 包含想要保留的列  0 和 3
my_column = [0, 3]
with open(input_file, 'r', newline='', encoding='UTF-8') as csv_reader:
    with open(output_file, 'w', newline='', encoding='UTF-8') as csv_writer:
        filereader = csv.reader(csv_reader)
        filewriter = csv.writer(csv_writer)
        for row in filereader:
            row_put = []
            for index_value in my_column:
                row_put.append(row[index_value])
            filewriter.writerow(row_put)

