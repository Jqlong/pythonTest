import sys


input_file = '../supplier_data.csv'
out_file = 'supplier_data_test.csv'

with open(input_file, 'r', encoding='UTF-8') as filereader:
    with open(out_file, 'w', encoding='UTF-8') as filewriter:
        # for之前的可以去掉
        content = filereader.readline().rstrip()
        content_list = content.split(',')
        print(content)  # 输出标题
        filewriter.write(','.join(map(str, content_list)) + '\n')  # 写标题
        for row in filereader:  # 文件的剩余
            row = row.rstrip()  # 是字符串
            row_list = row.split(',')   # 是列表
            print(row)
            filewriter.write(','.join(map(str, row_list)) + '\n')  # 写内容
        print(type(str(row_list)))

