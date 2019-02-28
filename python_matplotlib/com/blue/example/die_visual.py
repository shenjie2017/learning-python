import pygal

from die import Die

die1 = Die(8)
die2 = Die(6)

results = []
frequencies = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

max_sides = die1.num_sides + die2.num_sides

for value in range(2, max_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化显示
hist = pygal.Bar()
hist.title = "results of rolling 1000 times"
hist.x_labels = list(range(2,max_sides+1))
#['2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "result"
hist.y_title = "frequency of result"

hist.add("D6 + D8", frequencies)
hist.render_to_file("die_visual.svg")
