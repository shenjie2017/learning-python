import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 设置线条宽度
plt.plot(input_value, squares, linewidth=1)

# 设置图标标题，并为图标横纵轴加上标签
plt.title("square numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

# 显示图标
plt.show()
