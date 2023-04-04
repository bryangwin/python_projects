import pandas

s_data = pandas.read_csv("squirrel_data.csv")

gray_count = len(s_data[s_data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(s_data[s_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(s_data[s_data["Primary Fur Color"] == "Black"])

s_dic = {
    "Fur": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
    }

s_csv = pandas.DataFrame(s_dic)

s_csv.to_csv("s_data.csv")
