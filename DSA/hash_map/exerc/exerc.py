#https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/4_hash_table_exercise.md

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "nyc_weather.csv")

stock_price = []

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    
    def __setitem__(self, key, val):
        
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                
        if not found:
            self.arr[h].append((key,val))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


data = HashTable()
with open(file_path, "r") as f:
    for line in f:
        tokens = line.split(",")
        if(tokens[0] != 'date' and tokens[1] != 'temperature(F)'):
            key = tokens[0]
            val = int(tokens[1])
            data[key] = val 
                

"""
What was the average temperature in first week of Jan
"""

def get_average():
    count = 0
    for index, _ in enumerate(data.arr):
        for value in data.arr[index]:
            splitVal = value[0].split(" ")
            valueInt = int(splitVal[1])
            if(valueInt <= 7):
                count += value[1]
    return count / 7
       

average = get_average()

print(f"Média da primeira semana: {average:.2f}")

"""
What was the maximum temperature in first 10 days of Jan
"""

def maximum_temperature():
    max = 0
    for index, _ in enumerate(data.arr):
        for value in data.arr[index]:
            if value[1] > max:
                max = value[1]
            
    return max

max_temp = maximum_temperature()
print(max_temp)


#solution 
arr = []

with open(file_path,"r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")

sum_cont = sum(arr[0:7])/len(arr[0:7])

print(sum_cont)

maximum = max(arr[0:10])
print(maximum)

"""
What was the temperature on Jan 9?
"""
"""
What was the temperature on Jan 4?
"""

# def temp(day):
#     temperature = None
#     date = f"Jan {day}"
#     for index, _ in enumerate(data.arr):
#             for value in data.arr[index]:
#                 if(value[0] == date):
#                     temperature = value[1]

#     return temperature

# day9 = temp(9)
# day4 = temp(4)

# print(day9)
# print(day4)

print(data['Jan 9'])
print(data['Jan 4'])

