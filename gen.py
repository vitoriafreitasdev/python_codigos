print("\nIterators\n")
def remote_control_next():
    yield "fox"
    yield "espn"


itr = remote_control_next()
print(next(itr))
print(next(itr))

for c in remote_control_next():
    print(c)

print("\nGenerators\n")
## generators 

def fib():
    a, b = 0, 1
    while True:
        yield a 
        a, b = b, a+b


for f in fib():
    if f > 100:
        break
    print(f)

print("\nGenerators\n")

def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i

a = sq_numbers(3)

print("The square of numbers 1, 2, 3 are:")
print(next(a))
print(next(a))
print(next(a))

print("\nIterators\n")
l = iter(['Geeks', 'For', 'Geeks'])
print(next(l))
print(next(l))
print(next(l))