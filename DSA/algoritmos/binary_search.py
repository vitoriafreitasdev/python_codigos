from bubblesort import ordenar


lista = [5, 3, 1, 4, 9, 2]
lista_ord = ordenar(lista)

import bisect

def binary_search_bisect(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search_bisect(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

#

def bs(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == item:
            return middle
        elif guess > item:
            high = middle - 1
        else:
            low = middle + 1
    return None 

res = bs(lista_ord, 4)
print(lista_ord)
print(res)


#
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")







            
            