from multiprocessing import Pool
import time
def f(n):
    print(n)
    sum = 0
    for x in range(1000):
        sum += x*x 
    return sum

if __name__ == "__main__":

    t1 = time.time()
    p = Pool()
    result = p.map(f, range(10))
    p.close()
    p.join()
    print("Pool took: ", time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(10):
        result.append(f(x))
    
    print("Serial processing took: ", time.time() - t2)


"""
range(X) no p.map → Determina quantas vezes a função f será chamada E fornece o valor de n

range(Y) dentro de f → É fixo para cada chamada r e determina o trabalho interno de cada chamada
"""