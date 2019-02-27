list1 = ["kevin", 18, "jason", 25, "Luck", 20]
list2 = ["Bob", 30]

list3 = list1 + list2

print(list1)
print(list2)
print(list3)

print(list1[0])
print(list1[2:4])
print(list1[2:])
print(list1[-3:])
print(list1[:2])
print(list1[:])
print(list1[-1])
print(list1[-4])

print(list2 * 2)

list4 = list1[:]
list5 = list1

list4[0] = 'Bob'
list5[0] = 'old six'
print(list1)
print(list4)
print(list5)
print(list4[0].title(), list4[0].lower(), list4[0].upper())

list6 = ['a', 'd', 'E', 'g', 'F']
print(list6)
list6.sort()
print(list6)
list6.reverse()
print(list6)

for item in list6:
    print(item)

