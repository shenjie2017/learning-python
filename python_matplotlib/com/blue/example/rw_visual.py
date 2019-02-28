import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(50000)

rw.fill_walk()

#设置绘图窗口的尺寸
plt.figure(dpi=128,figsize=(10,6))

# plt.scatter(rw.x_values,rw.y_values,s=1)
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
