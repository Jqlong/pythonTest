import csv
"""通过列标题选取特定的列"""
input_file = '../supplier_data.csv'
output_file = 'supplier_data_test_7.csv'
my_column = ['Invoice Number', 'Purchase Date']
my_column_index = []
with open(input_file, 'r', newline='', encoding='UTF-8') as csv_reader:
    with open(output_file, 'w', newline='', encoding='UTF-8') as csv_writer:
        filereader = csv.reader(csv_reader)
        filewriter = csv.writer(csv_writer)
        header = next(filereader)
        for index_value in range(len(header)):  # 标题的长度遍历
            if header[index_value] in my_column:
                my_column_index.append(index_value)  # 产生标题的索引值

        filewriter.writerow(my_column)  # 将目标标题写入文件
        for row_list in filereader:  # 读取余下的每一行 row_list是一个列表
            print(row_list)  # 行中的所有数据
            row_list_output = []  # 保存每一行的值
            for index_values in my_column_index:   # 1和4
                row_list_output.append(row_list[index_values])  # 筛选特定列的数据
            filewriter.writerow(row_list_output)
        print(my_column_index)

