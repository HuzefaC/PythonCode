# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp_list = []
#     for row in data:
#         temp_list.append(row[1])
#     print(temp_list)

import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"]
average = sum(temp_list) / len(temp_list)
print(f"Average temperature: {round(average, 2)}")
print(f"Using pandas: {round(temp_list.mean(), 2)}")
print(f"Max temperature: {temp_list.max()}")

print(data[data.temp == data.temp.max()])
