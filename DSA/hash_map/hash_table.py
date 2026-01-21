import os
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_home_price = os.path.join(current_dir, "stock_prices.csv")
stock_price = []

with open(file_path_home_price, "r") as f:
    for line in f: 
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_price.append([day, price])

for element in stock_price:
    if element[0] == 'march 9':
        print(element[1])


stock_price = {}

with open(file_path_home_price, "r") as f:
    for line in f: 
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_price[day] = price 


print(stock_price)

print(stock_price['march 9'])

stock_price['march 12'] = 412

print(stock_price)