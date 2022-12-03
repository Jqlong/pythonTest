"""向表中插入新记录"""
import csv
import MySQLdb
from datetime import date, datetime

input_file = 'supplier_data.csv'

# 连接数据库
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', passwd='jiang')
c = con.cursor()

# 向suppliers表中插入数据
# 读取文件
file_reader = csv.reader(open(input_file, 'r', newline=''))
header = next(file_reader)
# 行遍历
for row in file_reader:
    data = []
    # 遍历列
    for column_index in range(len(header)):
        # 处理前4列
        if column_index < 4:
            # 剥去美元符号
            data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())
        else:
            # 处理日期列
            #
            a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))
            a_date = a_date.strftime('%Y-%m-%d')
            data.append(a_date)
    print(data)
    c.execute("""INSERT INTO Suppliers VALUES (%s,%s,%s,%s,%s);""", data)
con.commit()
print("")

# 查询Suppliers表
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    data = []
    for column_index in range(len(row)):
        data.append(str(row[column_index]))
    print(data)
