import time 

def calc_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number)
    end = time.time()
    print("calc_squared took " + str((end - start)*1000) + " mil sec")
    return result 

def calc_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end = time.time()
    print("calc_squared took " + str((end - start)*1000) + " mil sec")
    return result

# array = range(1, 1000000)
# out_range = calc_square(array)
# out_cube = calc_cube(array)

"""
Now using decorators
"""

import time 

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start)*1000) + " mil sec")
        return result
    
    return wrapper

@time_it
def calc_square2(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result 

@time_it
def calc_cube2(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1, 10)
out_range = calc_square2(array)
out_cube = calc_cube2(array)