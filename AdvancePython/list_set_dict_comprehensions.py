n = [1, 2, 3, 4, 5, 6, 7]
even = []

for i in n:
    if i % 2 == 0:
        even.append(i)

print(even)

#using list comprehensions 
even = [i for i in n if i % 2 == 0]
print(even)

squared = [i*i for i in n]
print(squared)

s = set([1, 2, 3, 4, 5, 2, 3])
print(s)

even = {i for i in s if i % 2 == 0}
print(even)

#dictionary comprehensions

cities=["mumbai", "new york", "paris"]
countries=["india", "usa", "france"]

z = zip(cities, countries)

for a in z:
    print(a)

d = {city:country for city, country in zip(cities, countries)}
print(d)

dic = {}
for c, cc in  zip(cities, countries):
    dic[c] = cc

print(dic)

#study lambda