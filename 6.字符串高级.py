# _*_ coding : utf-8 _*_
# @Time : 2022/10/6 12:09
# @Author : 邓浩
# @File : 字符串高级
# @Project : python-basic
str = "str"

# len length的缩写 长度
print("字符串的长度是：", len(str))

# find 查找内容是否存在，如果存在返回字符串中第一次出现的下标
print(str.find('t'))

# startswith endswith 判断字符串是不是以谁谁谁开头
print(str.startswith('s'))
print(str.endswith('s'))

str1 = "aaabbb"
# count 计算出现次数
print(str1.count('a'))

# replace 替换指定内容
print(str1.replace('a', 'b'))

# spilt 切割字符串
str2 = "1#2#3#4"
print(str2.split('#'))

# lower 将大写字母改成小写字母
str3 = "CHINA"
print(str3.lower())

# upper 将小写字母改成大写字母
str4 = "china"
print(str4.upper())

# strip 空格处理
str5 = "  d"
print(str5)
print(str5.strip())

# join 字符串拼接
str6 = "a"
# test = ['sdas', 'asdas', 'asdas']
print(str6.join('hello'))
