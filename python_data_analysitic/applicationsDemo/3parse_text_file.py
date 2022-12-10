"""为文本文件中数据的任意数目分类计算统计量"""
input_file = 'mysql_server_error_log.txt'
output_file = 'output/3pp_output.csv'
# 创建空字典
message = {}
# 保存错误信息
notes = []
with open(input_file, 'r', newline='') as text_file:
    # 遍历行
    for row in text_file:
        # 包含Note的行就是包含错误消息的行。
        if '[Note]' in row:
            # 最多使用4个空格拆分4次
            row_list = row.split(' ', 4)
            # 取出第一个信息
            day = row_list[0].strip()
            # 取出第5个信息
            note = row_list[4].strip('\n').strip()
            # 如果原本没这个消息
            if note not in notes:
                # 就添加进列表中
                notes.append(note)
            # 检查日期是否是message的一个键
            if day not in message:
                # 添加多字典中，并创建一个空字典
                message[day] = {}
            # 检查note中的错误信息是否是这个日期的值
            if note not in message[day]:
                message[day][note] = 1
            else:
                # 在某一天出现多次的情况
                message[day][note] += 1
# 打开输出文件
filewriter = open(output_file, 'w', newline='')
# 标题
header = ['Date']
# extend将列表notes中的内容扩展到header中
header.extend(notes)
# 将列表变量header中的内容写入输出文件之前转换成一个长字符串。
header = ','.join(map(str, header)) + '\n'
print(header)
# 写
filewriter.write(header)
# 遍历字典的键值
for day, day_value in message.items():
    row_of_output = []
    # 第一列是日期
    row_of_output.append(day)
    for index in range(len(notes)):
        if notes[index] in day_value.keys():
            row_of_output.append(day_value[notes[index]])
            # 个数
            print(day_value[notes[index]])
        else:
            row_of_output.append(0)
    output = ','.join(map(str, row_of_output)) + '\n'
    print(output)
    filewriter.write(output)
filewriter.close()




