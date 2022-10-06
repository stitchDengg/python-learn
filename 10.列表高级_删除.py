# _*_ coding : utf-8 _*_
# @Time : 2022/10/6 18:44
# @Author : 邓浩
# @File : 10.列表高级_删除
# @Project : python-basic'

# del：根据下标进行删除 pop：删除最后一个元素 remove：根据元素的值进行删除
movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
print('‐‐‐‐‐‐删除之前‐‐‐‐‐‐movieName=%s' % movieName)
del movieName[2]
print('‐‐‐‐‐‐删除之后‐‐‐‐‐‐movieName=%s' % movieName)

movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
print('‐‐‐‐‐‐删除之前‐‐‐‐‐‐movieName=%s' % movieName)
movieName.pop()
print('‐‐‐‐‐‐删除之后‐‐‐‐‐‐movieName=%s' % movieName)

movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
print('‐‐‐‐‐‐删除之前‐‐‐‐‐‐movieName=%s' % movieName)
movieName.remove('指环王')
print('‐‐‐‐‐‐删除之后‐‐‐‐‐‐movieName=%s' % movieName)