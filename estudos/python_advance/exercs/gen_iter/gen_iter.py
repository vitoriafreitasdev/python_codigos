#https://medium.com/@colebuildanddevelop/python-generators-versus-iterators-d8e35024a590

## generators 
"""
a generator is a function that returns an iterable. An iterable is an object capable of producing its members one at a time (lists, tuples, strings, etc.). However, the iterable returned from a generator is different in that it is considered a generator object. When we begin iterating over a generator object, we are not merely reading from memory. Instead, we are executing code in the body of our generator function for each iteration. The most defining feature of a python generator is the “yield” statement. The main difference between yield and return statements is that a yield statement does not terminate the function. A yield statement pauses the operation and remembers the state, and can later continue on further iterations.
"""

def reverse_str(str):
    for i in range(len(str)-1, -1, -1):
        yield str[i]

# for char in reverse_str("hello"):
#     print(char)

## iterator 

"""
iterators versus iterables:
iterable is an object capable of being iterated. An iterator is an object that is used to iterate over an iterable. All iterator objects have a “__next__” method implementation that is used to return the next item in the iterable, as well as raise “StopIteration” to signal that there is no more iteration to be done. The __next__() method will also update the object’s state to point to the next value in the iterable. Iterables and some iterators have an “__iter__” method that is used to return an iterator.
"""

class count_to_ten:
    def __init__(self):
        self.max = 10
    
    def __iter__(self):
        self.n = 0
        return self 
    
    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n 
        else:
            raise StopIteration
        
count_obj = count_to_ten()
count_iter = iter(count_obj)

# for i in count_iter:
#     print(i)


#Should I use an iterator or a generator?

"""
A generator is initialized as a function, whereas an iterator requires writing a class. Therefore generators are not only easier to implement but also increase our code’s readability.

Iterators are useful when we need to extend any object that needs to be iterated over. Or if we need a class that has complex state management and other methods. Otherwise, for the majority of cases, a generator is suited.
"""

arr = ["maça", "pera", "uva", "banana"]

#Iterator 

itr = iter(arr)
# print(next(itr))
for i in range(len(arr)):
    print(next(itr))

#generator 

def example_gen(arr):
    for i in range(len(arr)):
        yield arr[i]
        

n = example_gen(arr)


for i in n:
    print(i)

class Iter_class:
    def __init__(self, val):
        self.val = val 
        self.index = -1 
    
    def __itr__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index  < len(self.val):
            return self.val[self.index]
        else:
            raise StopIteration
        

iter_obj = Iter_class(["camisa", "calça", "joia", "relogio", "tenis"])
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

