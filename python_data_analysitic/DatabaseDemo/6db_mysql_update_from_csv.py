"""更新表中记录"""
import csv
import MySQLdb

input_file = 'data_for_updating_mysql.csv'
# 链接数据库
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', passwd='jiang')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter=',')
header = next(file_reader)
# 读文件
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)
    c.execute("""UPDATE Suppliers SET Cost=%s, Purchase_Date=%s WHERE Supplier_Name=%s;""", data)
con.commit()

# 查询表
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    data = []
    for column_index in range(len(row)):
        data.append(str(row[column_index]))
    print(data)






