# with open('../tip', encoding='UTF-8') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

with open('../tip.txt', encoding='UTF-8') as file_object:
    lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

pi_string=''
for line in lines:
    pi_string += line.strip()

index = input("输入你想要查询的汉字：\n")
if index in pi_string:
    print("在")
else:
    print("不在")