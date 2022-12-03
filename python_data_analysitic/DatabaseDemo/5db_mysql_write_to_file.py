"""查询一个表并将输出写入csv文件"""
import csv
import MySQLdb

output_file = 'output/5output.csv'
# 连接数据库
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', passwd='jiang')
c = con.cursor()
# 写文件
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')

header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
# 写标题
filewriter.writerow(header)
# 查询
c.execute("""SELECT * FROM Suppliers WHERE Cost > 700.0;""")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)
