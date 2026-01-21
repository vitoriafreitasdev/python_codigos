from multiprocessing import Pool
import time

def f(n):
    # Trabalho mais leve para ver melhor o efeito da paralelização
    print(n)
    return n * n  # Apenas um cálculo simples

if __name__ == "__main__":
    
    # Teste com Pool
    t1 = time.time()
    with Pool() as p:
        result = p.map(f, range(10))
    print("Pool took: ", time.time() - t1)

    print(result)
    
    # # Teste serial
    # t2 = time.time()
    # result = []
    # for x in range(10):
    #     result.append(f(x))
    # print("Serial processing took: ", time.time() - t2)