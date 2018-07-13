# -*- coding:UTF-8 -*-

prime = set()
allnumber = set()

for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime.add(i)    # 未执行break时才会执行

    allnumber.add(i)    # 每次退出循环时都会执行


print allnumber
print prime