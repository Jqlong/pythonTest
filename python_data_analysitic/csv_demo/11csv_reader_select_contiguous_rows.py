import csv
"""选取特定的行"""
input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_11.csv'
row_count = 0  # 用于追踪行编号
with open(input_file, 'r', encoding='UTF-8', newline='') as csv_reader:
    with open(output_file, 'w', encoding='UTF-8', newline='') as csv_writer:
        filereader = csv.reader(csv_reader)
        filewriter = csv.writer(csv_writer)
        for row in filereader:
            if 3 <= row_count <= 15:
                filewriter.writerow([value.strip() for value in row])
                print([value.strip() for value in row])
            row_count += 1

