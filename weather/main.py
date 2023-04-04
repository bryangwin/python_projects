import csv
import pandas

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
    
#     print(temps)

data = pandas.read_csv("weather_data.csv")



monday = data[data.day == "Monday"]

f = (int(monday.temp)) * 9/5 + 32

print(f)
