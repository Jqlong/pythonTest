a_list = [1, 2, 3]
print("Output 1:{}".format(a_list))
print("Output 2:{}".format(len(a_list)))
print("Output 2:{}".format(max(a_list)))
print("Output 2:{}".format(min(a_list)))
another_list = ['printer', 5, ['star', 'circle', 9]]
print("Output 1:{}".format(another_list))
print("Output 1:{}".format(len(another_list)))

my_lists = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 4, 1, 3]]
my_lists_sorted = sorted(my_lists, key=lambda index_value:index_value[3])
