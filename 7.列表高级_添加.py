# _*_ coding : utf-8 _*_
# @Time : 2022/10/6 14:41
# @Author : 邓浩
# @File : 7.列表高级
# @Project : python-basic

# append  添加
food_list = ['1', '2']
print(food_list)
food_list.append('3')
print(food_list)

# insert  插入
char_list = ['a', 'c', 'd']
# index的值就是你想插入的数据的那个下标
char_list.insert(1, 'b')
print(char_list)

# extend 通过extend可以将一个列表中的元素逐一追加到列表中
num_list = [1, 2, 3]
num1_list = [4, 5, 6]

# 参数必须是可迭代对象 例如元组和列表
num_list.extend(num1_list)
print(num_list)
