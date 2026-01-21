import time 
import threading

def calc1(n):
    print("iniciando calc1")
    res = 0
    for i in range(n):
        time.sleep(0.6)
        res += n*i
    print("Res da calc1", res)


def calc2(n):
    print("iniciando calc2")
    res = 0
    for i in range(n):
        time.sleep(0.6)
        res += n*i*2
    print("Res da calc2", res)


def calc3(n):
    print("iniciando calc3")
    res = 0
    for i in range(n):
        time.sleep(0.6)
        res += n*i*i*2/2
    print("Res da calc3", res)

def calc4(n):
    print("iniciando calc4")
    res = 0
    for i in range(n):
        time.sleep(0.6)
        res += n*i*i / 2
    print("Res da calc4", res)

def calc5(n):
    print("iniciando calc5")
    res = 0
    for i in range(n):
        time.sleep(0.6)
        res += n*i*i*2
    print("Res da calc5", res)


if __name__ == '__main__':
    n = 2 
    
    t1 = threading.Thread(target=calc1, args=(n,))
    t2 = threading.Thread(target=calc2, args=(n,))
    t3 = threading.Thread(target=calc3, args=(n,))
    t4 = threading.Thread(target=calc4, args=(n,))
    t5 = threading.Thread(target=calc5, args=(n,))

    time1 = time.time()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    time2 = time.time()
    
    calc1(n)
    calc2(n)
    calc3(n)
    calc4(n)
    calc5(n)
    time3 = time.time()
    print("Usando threading: ",time2-time1)
    print("Sem: ", time3-time2)
