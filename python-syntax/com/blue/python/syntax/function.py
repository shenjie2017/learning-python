# -*- coding:UTF-8 -*-

def newList(list1,list2):
    return list1+list2

def appendList(list1,list2):
    return list1.extend(list2)

# 带默认参数
def defaultParamFunction(name,age=18,sex='man'):
    print name,age,sex

#带可变参数
def printInfo(appName,*args):
    print 'appName:',appName
    print args
    print "param type is ",type(args)

    for var in args:
        print var

list1 = [1,2,3,4]
list2 = [5,6,7]
list3 = [8,9]

print type(newList)
print type(appendList)

print list1
print newList(list1,list2)
print list1

print list3
print appendList(list3,list2)
print list3

defaultParamFunction('kevin')
defaultParamFunction('json',24)
defaultParamFunction('luck',22,'men')

printInfo("testFunction",'zhangsan',28,'man')

#lambda快速定义函数
sum = lambda arg1,arg2:arg1+arg2
print type(sum)
print sum(1,2)

# 生成元组
makeTuple = lambda arg1,arg2:(arg1,arg2)
print makeTuple('width','height')

def outFunction(func,x,y):
    return func(x,y)

print outFunction(lambda x,y:x+y , 100,200)

