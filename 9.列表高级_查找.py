# _*_ coding : utf-8 _*_
# @Time : 2022/10/6 18:22
# @Author : 邓浩
# @File : 9.列表高级_查找
# @Project : python-basic
# in 是判断某一个元素是否在某一个列表中
food_list = ['锅包肉', '李庄白肉', '东北乱炖']

# 判断控制台输入的那个数据 是否在列表中
"""food = input("请输入您想吃的食物")
if food in food_list:
    print('在')
else:
    print('不在')"""


# not in 判断是否不再

ball_list = ['台球','篮球']

# 在控制台尚输入你喜欢的球类 然后判读是否不在这个列表中

ball = input("输入你喜欢的球类\n")
if ball not in ball_list:
    print("不在")
else:
    print('在')
