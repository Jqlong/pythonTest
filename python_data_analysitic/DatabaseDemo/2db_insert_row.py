"""向表中插入新纪录"""
import csv
import sqlite3

# csv输入文件的路径和文件名
input_file = 'supplier_data.csv'
# 创建SQLite3内存数据库
con = sqlite3.connect('output/Suppliers.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers
                    (Supplier_Name VARCHAR(20),
                    Invoice_Number VARCHAR(20),
                    Part_Number VARCHAR(20),
                    Cost FLOAT,
                    Purchase_Date DATE
                    );"""
c.execute(create_table)
con.commit()

# 读取csv文件
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
# 读取标题行
print(type(file_reader))
header = next(file_reader, None)
# 遍历行
for row in file_reader:
    data = []
    # 遍历列
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    # 插入数据
    c.execute("INSERT INTO Suppliers VALUES (?,?,?,?,?);", data)
print(type(row))  # 列表
con.commit()
print('')
# 查询
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)


