import csv

input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_4.csv'
important = ['1/20/14', '1/30/14']
with open(input_file, 'r', newline='', encoding='UTF-8') as csv_reader:
    with open(output_file, 'w', newline='', encoding='UTF-8') as csv_writer:
        filereader = csv.reader(csv_reader)
        filewriter = csv.writer(csv_writer)
        header = next(filereader)  # 读标题
        filewriter.writerow(header)
        for row in filereader:
            a_data = row[4]
            if a_data in important:
                filewriter.writerow(row)
        print(type(csv_reader))
        print(type(filereader))
        print(type(row))


