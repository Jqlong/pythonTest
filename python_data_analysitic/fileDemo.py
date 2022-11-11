import sys
import re
from math import exp, log, sqrt
import glob
import os


# 读取多个文本文件

filepath = '../'

for input_file in glob.glob(os.path.join(filepath, '*.txt')):  # 筛选txt文件
    with open(input_file, 'r', newline='', encoding='UTF-8') as filereader:
        content = filereader.readline()
        print(content.rstrip())
        for content in filereader:
            print(content.rstrip())

