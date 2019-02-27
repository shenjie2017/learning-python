# -*- coding:UTF-8 -*-

print("test1:")
with open("test01.dat") as file:
    print(file.read())

print("test2:")
with open("test01.dat") as file:
    for line in file.readlines():
        print(line)

print("test3:")
with open("test01.dat") as file:
    for line in file.readlines():
        print(line.strip())

print("test4:")
with open("test01.dat","a") as file:
    file.write("\nthis test record.")

print("test5:")
with open("test02.dat") as file:
    for line in file.readlines():
        print(line.strip())

print("test6:")
with open("test02.dat", "w") as file:
    file.write("this test record.")