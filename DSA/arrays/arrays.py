"""
Store apples  stock price for days and answer
"""

stock_prices = [298, 305, 320, 301, 292]
stock_prices[0] #price for day 1
stock_prices[1] #price for day 2
def find_day_prince(price):
    for i in range(len(stock_prices)):
        if stock_prices[i] == price:
            return i


print(find_day_prince(301))

def find_price_binary_way(array, item):
    array_sorted = sorted(array)
    print("Array ordenado: ", array_sorted)
    baixo = 0
    alto = len(array_sorted) - 1
    while baixo <= alto:
        meio = (baixo+alto) // 2
        chute = array_sorted[meio]
        if chute == item:
            return meio 
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None 


#print(find_price_binary_way(stock_prices, 301))



# #Insert new price 284 at index 1
# stock_prices.insert(1, 284)

# #filas 
# from collections import deque

# # Cria uma fila (deque)
# fila = deque()

# # Adiciona elementos (enqueue)
# fila.append('A')
# fila.append('B')
# fila.append('C')
# print(f"Fila: {fila}") # Saída: Fila: deque(['A', 'B', 'C'])

# # Remove elementos (dequeue - FIFO: First-In, First-Out)
# primeiro_elemento = fila.popleft()
# print(f"Removido: {primeiro_elemento}") # Saída: Removido: A
# print(f"Fila após remover: {fila}") # Saída: Fila após remover: deque(['B', 'C'])

# # Verifica se está vazia e o tamanho
# print(f"Está vazia? {not fila}") # Saída: Está vazia? False
# print(f"Tamanho: {len(fila)}") # Saída: Tamanho: 2

"""Execise"""

#Array for expenses, january to may

expenses = [2200, 2350, 2600, 2130, 2190]

#1. In Feb, how many dollars you spent extra compare to January?

feb_extra_jan = expenses[1] - expenses[0]
print("Feb extra dollars compare to Jan: ", feb_extra_jan)

#2. Find out your total expense in first quarter (first three months) of the year.
total = 0
for i in range(3):
    total += expenses[i]
print("Total expense in first quarter: ", total)

#3. Find out if you spent exactly 2000 dollars in any month

def spend(n):
    for expense in expenses:
        if expense == n:
            return True
        else: 
            return False 

spend_2000 = spend(2000)      
print(f"I spend more exactly 2000: {"Yes" if spend_2000 else "No"}")
#or:
#print("Did I spent 2000$ in any month? ", 2000 in exp) # False

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expenses.append(1980)
print(expenses)

#5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

new_n = expenses[3] - 200
expenses[3] = new_n
print(expenses)

#2.You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
#1. Length of the list
print("List len: ", len(heros))
# 2. Add 'black panther' at the end of this list
heros.append("Black panther")
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
heros.pop()
heros.insert(3, "black panther")
print(heros)

#4. Now you don't like thor and hulk because they get angry easily :)
#So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#Do that with one line of code.
 
heros.remove('thor'); heros.remove('hulk'); heros[1] = 'doctor strange'
#heros[1:3]=['doctor strange']
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros.sort()
print(heros)

#3- Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max_number = int(input("Max number: "))

items = [n**2 for n in range(max_number) ]
odd_numbers = []
for item in items:
    if item % 2 != 0:
        odd_numbers.append(item)

print("items: ", items)
print("odd_numbers: ", odd_numbers)

#or:
for i in range(1, max_number):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers 2: ", odd_numbers)


#using random:
import random

random_n = random.sample(range(1, 31), max_number) 
print("random_n: ", random_n)

random_list = [random.randint(1, 100) for _ in range(10)]
print("random_list", random_list)