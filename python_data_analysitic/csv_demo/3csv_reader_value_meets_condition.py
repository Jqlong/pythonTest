import csv
import sys

input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_3.csv'

with open(input_file, 'r', encoding='UTF-8', newline='') as csv_reader:
    with open(output_file, 'w', encoding='UTF-8', newline='') as csv_writer:
        filereader = csv.reader(csv_reader)
        filewriter = csv.writer(csv_writer)
        header = next(filereader)  # 读出输入文件的第一行
        filewriter.writerow(header)  # 写标题

        for row in filereader:
            supplier = str(row[0]).strip()
            # print(supplier)
            cost = str(row[3].strip('$').replace(',', ''))
            if supplier == 'Supplier Z' or float(cost) > 600.0:
                filewriter.writerow(row)
                print(f"{supplier},{cost}")
            # filewriter.writerow(row)  # 方法一

        # for row in csv_reader:
        #     print(row.strip())
        #     csv_writer.write(row)  # 方法二


