"""
Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.
"""

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

##

def myDecorator(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs) * f(*args, **kwargs)
        return result
    return wrapper

@myDecorator
def countN(n):
   return n + 10
@myDecorator
def countN2(n, x, y):
   return (n / x) * y 

count_call = countN(10)
count_call2 = countN2(10, 2, 3)

print(count_call)
print(count_call2)

##

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())


##

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

##

def return_items(val):
    def f(func):
        def wrapper(*args, **kwargs):
            if val == "keys":
                return func(*args, **kwargs).keys()
            if val == "values":
                return func(*args, **kwargs).values()
            else:
                return func(*args, **kwargs).items()
        return wrapper
    return f 

@return_items("items")
def dictionary(arr):
   return {key:value for key, value in enumerate(arr)}

arr = ["roupa", "acessorio", "chaves", "bone", "brincos", "relogios"]
dictionary_test = dictionary(arr)
print(dictionary_test)

##

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

##
#Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

def changecase(func):
  def myinner():
    return func().upper()
  return myinner
#But, when a function is decorated, the metadata of the original function is lost.
@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

#To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)