import re
from math import exp, log, sqrt

string = "The quick brown fox jumps over the lazy dog."
string_list1 = string.split()  # 分割成列表
pattern = re.compile(r"The", re.I)   # 编译成正则表达式，re.I表示不区分大小写
count = 0
for word in string_list1:
    if pattern.search(word):
        count += 1
print("Output 1: {0:d}".format(count))

pattern2 = re.compile(r"(?P<match_word>The)", re.I)
print("Output 2:")
for word in string_list1:
    if pattern2.search(word):
        print("{:s}".format(pattern2.search(word).group('match_word')))

