#!/usr/bin/python
# coding:UTF-8

if True:
    print("true")  # 如果为真(需指定为带有中文的编码格式，例如coding:UTF-8)
else:
    print("false")
    print("is false")

print("answer ok")
print("end")

names = ['zhangsan', 'lisi', 'wangwu']

new_name = ['zhangsan', 'kevin']

for name in new_name:
    if name in names:
        print(name + ' is in names')
    else:
        print(name + ' is not in names')

print(name)
