import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# plt.scatter(x_values, y_values,c='red',edgecolors='none', s=1)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=1)

plt.title("square numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of value", fontsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
#plt.savefig("squares_scatter.png", bbox_inches='tight')