"""为CSV文件中数据的任意数目分类计算统计量"""
import csv
from datetime import date, datetime


# 定义函数，用于返回两个日期之间的天数间隔
def date_diff(date1, date2):
    try:
        # 转换成字符串后按空格进行分隔，保留字符串最左边的部分。
        # 52 days
        diff = str(datetime.strptime(date1, '%m/%d/%Y') - datetime.strptime(date2, '%m/%d/%Y')).split()[0]
    # 不要用裸异常
    except:
        diff = 0
    if diff == '0:00:00':
        diff = 0
    print(diff)
    return diff


# 输入文件
input_file = 'customer_category_history.csv'
# 输出
output_file = 'output/2app_output.csv'
# 空字典，保存需要的信息
packages = {}
# 客户姓名
previous_name = 'N/A'  # 赋初值
# 服务包类
previous_package = 'N/A'
# 服务包日期
previous_package_date = 'N/A'
# 是否为输入文件的第一行
first_row = True
# 获取当前的日期
today = date.today().strftime('%m/%d/%Y')
# 打开文件
with open(input_file, 'r', newline='') as input_csv_file:
    filereader = csv.reader(input_csv_file)
    # 获取标题
    header = next(filereader)
    # 遍历行
    for row in filereader:
        # 取出第一列的值姓名
        current_name = row[0]
        # 第二列服务包类型
        current_package = row[1]
        # 第四列日期
        current_package_date = row[3]
        # 检验是不是字典中的值
        if current_name not in packages:
            # 添加到字典中，将名字键 设置为一个空的字典
            packages[current_name] = {}
        if current_package not in packages[current_name]:
            # {'John Smith':{'Bronze':0}}
            # {'John Smith':{'Silver':0, 'Bronze':52}}
            packages[current_name][current_package] = 0
        # 检验当前姓名是否不等于previous_name，如果是
        if current_name != previous_name:
            # 检验是否处于第一行
            if first_row:
                first_row = False
            else:
                # 计算日期差
                diff = date_diff(today, previous_package_date)
                if previous_package not in packages[previous_name]:
                    packages[previous_name][previous_package] = int(diff)
                else:
                    packages[previous_name][previous_package] += int(diff)
        # 如果不是
        else:

            diff = date_diff(current_package_date, previous_package_date)
            packages[previous_name][previous_package] += int(diff)
        previous_name = current_name
        previous_package = current_package
        previous_package_date = current_package_date
header = ['Customer Name', 'Category', 'Total Time (in Days)']
# 写文件
with open(output_file, 'w', newline='') as output_csv_file:
    filewriter = csv.writer(output_csv_file)
    filewriter.writerow(header)
    for customer_name, customer_name_value in packages.items():
        for package_category, package_category_value in packages[customer_name].items():
            row_of_output = []
            print(customer_name, package_category, package_category_value)
            row_of_output.append(customer_name)
            row_of_output.append(package_category)
            row_of_output.append(package_category_value)
            filewriter.writerow(row_of_output)





