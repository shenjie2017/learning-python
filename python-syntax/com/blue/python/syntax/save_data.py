import json

names = ["zhangsan", "lisi", "wangwu", 666]
zhangsan_info = {"name": "zhangsan", "age": 18, "sex": "man"}
lisi_info = {"name": "lisi", "age": 24, "sex": "woman"}

peoples = [zhangsan_info,lisi_info]

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

with open("test05.json", "w") as file:
    json.dump(peoples, file)

with open("test05.json", "r") as file:
    arr = json.load(file)
    print(arr)