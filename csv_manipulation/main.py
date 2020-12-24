# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp_list = []
#     for row in data:
#         temp_list.append(row[1])
#     print(temp_list)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"]
# average = sum(temp_list) / len(temp_list)
# print(f"Average temperature: {round(average, 2)}")
# print(f"Using pandas: {round(temp_list.mean(), 2)}")
# print(f"Max temperature: {temp_list.max()}")
#
# print(data[data.temp == data.temp.max()])

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black_squirrel_count = data["Primary Fur Color"][data["Primary Fur Color"] == "Black"].count()
cinnamon_squirrel_count = data["Primary Fur Color"][data["Primary Fur Color"] == "Cinnamon"].count()
gray_squirrel_count = data["Primary Fur Color"][data["Primary Fur Color"] == "Gray"].count()

data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
