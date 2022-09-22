# 通过占位的方式，完成拼接
name = "邓浩"
sex = "男"
message = "%s性别是%s，学校是cuc" % (name, sex)
print(message)

# 通过占位的方式，完成数字和字符串的拼接
# %s %d %f 分别表示字符串 整形 浮点型的占位符
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资%s" % (class_num, avg_salary)
print(message)
message = "Python大数据学科，北京%d期，毕业平均工资%d" % (class_num, avg_salary)
print(message)

name = "邓浩"
birthDay = 10.12
birthYear = 1999
message = "%s出生于%d年%f日" % (name, birthYear, birthDay)
print(message)

# 利用m.n控制精度 m代表数据的宽度 n代表数据的精度
message = "%s出生于%5d年%.2f日" % (name, birthYear, birthDay)
print(message)
