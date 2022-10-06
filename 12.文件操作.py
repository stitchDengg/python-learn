# _*_ coding : utf-8 _*_
# @Time : 2022/10/6 19:16
# @Author : 邓浩
# @File : 12.文件操作
# @Project : python-basic
# f = open('test.txt','w')
#
# f.write('hello world, i am here!\n' * 5)
#
# f.close()


import json
file = open('test.txt','w')
names = ['zhangsan', 'lisi', 'wangwu', 'jerry', 'henry', 'merry', 'chris']
res = json.dumps(names)

file.write(res)
file.close()

# dump方法可以接收一个文件参数，在将对象转换成为字符串的同时写入到文件里
json.dump(names,file)