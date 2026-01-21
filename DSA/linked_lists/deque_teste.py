from collections import deque

lista = deque()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

lista.popleft()

print(lista)

lista.appendleft(1)
print(lista)


new_list = [1, 2, 4, 4, 5, 3]

new_deque = deque(new_list)
new_set = set(new_list)
print(new_deque)
print(new_set)
