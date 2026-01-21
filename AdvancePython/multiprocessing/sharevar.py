#Sharing variable in differents process

import time
import multiprocessing


def calc_square(numbers, result, v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        # result.append(n*n) does not work in multiprocessing array
        result[idx] = n*n

    print("Inside process: ",  result[:])

if __name__ == "__main__":
    arr = [2,3,8]
    result = multiprocessing.Array('i', 3) # i is the type (integer) and 3 is the size
    v = multiprocessing.Value('d', 0.0)
    p1 = multiprocessing.Process(target=calc_square, args=(arr, result, v))

    p1.start()

    p1.join()

    print("Ouside process: ", result[:])
    print(v.value)

    print("Done!")