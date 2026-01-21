import time
def meu_decoraor(f):
    def wrapper():
        print("Antes")
        f()
        print("depois")
    return wrapper

@meu_decoraor
def minha_funcao():
    print("Conclui")


minha_funcao()

##

def time_f(f):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        res = f(*args, **kwargs)
        fim = time.time()
        return res, fim - inicio
    return wrapper

@time_f
def my_f(n):
    time.sleep(2)
    return n * n 


# res, tempo = my_f(10)
# print(res, tempo)

##

def repetir(n):
    def repetir_decorator(f):
        def wrapper():
            for i in range(n):
                f()
        return wrapper
    return repetir_decorator
@repetir(3)
def funcao_teste():
    print("ola")

funcao_teste()


##

import functools

# Apenas use o lru_cache diretamente - ele JÁ É um decorator de cache!
@functools.lru_cache(maxsize=None)  # maxsize=None = cache ilimitado
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Calcula cada valor apenas uma vez
print(fibonacci(10))  # Usa cache - cálculo instantâneo