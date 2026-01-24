
def ordenar(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

lista = [5, 3, 1, 4, 9, 2]
lista_ord = ordenar(lista)

print(lista_ord)
