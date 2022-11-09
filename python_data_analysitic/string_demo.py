print("Output 1: {:s}".format("sfsdfasdfs\
adfadf\
sdfsasdf\
fasdfa"))  # 用于将长字符串分行，整个打印

# *用于将字符串重复一定的次数
print("Output 2: {0} {1}{2}".format("She is", "very "*4, "beautiful."))

# 使用split分隔字符串
string1 = "My deliverable is due in May"
string_list1 = string1.split()
# 使用前两个空格进行拆分
string_list2 = string1.split(" ", 2)
print("Output 3: {0}".format(string_list1))
print("Output 4: First:{0} Second:{1} Third:{2}".format(string_list2[0], string_list2[1], string_list2[2]))
print("Output 5: {0}".format(string_list2))

string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
string7 = "Here's what Happens when You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))
string5 = "here's WHAT Happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string5.capitalize()))
string5_list = string5.split()
print("Output #37 (on each word):")
for word in string5_list:
    # 使用end=“” 不换行
    print("{0:s} ".format(word.capitalize()), end="")
