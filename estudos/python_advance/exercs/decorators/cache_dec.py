from functools import cache


#Cache:
#Store all the inputs with their outputs
#For each new input, check to see if its been before and if so return the result it had last time

@cache
def is_it_prime(num) -> bool:
    print("Calculating...", num)
    return all([num % i for i in range(2, num)])

print(is_it_prime(150000000))
print(is_it_prime(150000000))


