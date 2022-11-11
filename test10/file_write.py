file_path = '../tip.txt'
with open(file_path, 'a', encoding="UTF-8") as file_object:
    file_object.write("10.2\n")
    file_object.write("\t1.write()方法写入文件")
