
import multiprocessing
import threading
import time

def fatorial(n):
    if n == 0:
        return 1
    
    return n * fatorial(n - 1)

print(fatorial(5))

if __name__ == "__main__":
    n = 20
    p1 = multiprocessing.Process(target=fatorial, args=(n,))
    temp1 = time.time()
    p1.start()
    p1.join()
    temp3 = time.time()
    print("Multiprocessing tempo: ", temp3 - temp1)
    
    t1 = threading.Thread(target=fatorial, args=(n,))
    
    temp = time.time()
    t1.start()
    t1.join()
    temp2 = time.time()

    print("Threading tempo: ", temp2 - temp)

    if temp2 - temp > temp3 - temp1:
        print("Threading foi mais lenta")
    else:
        print("Multiprocessing foi mais lenta")
    
#Entender o porque de uma ser mais rapida que a outra