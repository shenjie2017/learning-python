import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = "..\data\death_valley_2014.csv"

with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(str(index), column_header)

    dates = []
    highs = []
    lows = []
    for row in reader:
        try:
            current_time = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_time, "missing data",row)
        else:
            dates.append(current_time)
            highs.append(high)
            lows.append(low)

#    print(highs)


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 让x的日期斜着
fig.autofmt_xdate()

plt.title("2014 daily high and low temperatures", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperatures(F)", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
