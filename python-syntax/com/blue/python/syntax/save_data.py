import json

names = ["zhangsan", "lisi", "wangwu", 666]
zhangsan_info = {"name": "zhangsan", "age": 18, "sex": "man"}

with open("test03.json", "w") as file:
    json.dump(zhangsan_info, file)

with open("test03.json", "r") as file:
    info = json.load(file)
    print(info)

with open("test04.json", "w") as file:
    json.dump(names, file)

with open("test04.json", "r") as file:
    arr = json.load(file)
    print(arr)
