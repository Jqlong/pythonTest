empty_dict = {}
a_dict = {'one': 1, 'two': 2, 'three': 3}
print("{}".format(a_dict))
print("{!s}".format(a_dict))   # !s转换成字符串

print("Output 3:{}".format(a_dict['one']))   # 使用键引用特定值
print("Output 4:{}".format(a_dict.keys()))
print("Output 4:{}".format(a_dict.values()))
print(type(a_dict.keys()))
lists = list(a_dict.keys())  # 转换成列表
print(lists)

