import csv
import glob
import os

input_path = '../'
file_count = 0
# 路径下所有的文件。
# join()函数将路径和文件选择条件结合在一起.
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    row_count = 1;
    with open(input_file, 'r', newline='', encoding='UTF-8') as csv_reader:
        filereader = csv.reader(input_file)
        header = next(filereader, None)
        for row in filereader:
            row_count += 1

    # os.path.basename 返回path的基本文件名
    # 打印文件名、文件行数、文件的列数
    print('{0!s}:\t{1:d} rows \t{2:d} columns'. \
          format(os.path.basename(input_file), row_count, len(header)))
    file_count += 1

# 是一个输入列表，可用于迭代
print(glob.glob(os.path.join(input_path, 'sales_*')))
print('Number of files:{0:d}'.format(file_count))
