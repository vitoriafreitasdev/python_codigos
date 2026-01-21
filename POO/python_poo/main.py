
from car import Car

class Car_company:
    car_numbers = 0
    def __init__(self):
        self.cars = []
        Car_company.car_nums()

    def add_car(self, car):
        self.cars.append(car)
    @classmethod
    def car_nums(cls):
        cls.car_numbers += 1

car1 = Car( "Volks", 2001, "blue", False, "car")
car2 = Car( "Honda", 2021, "black", True, "car")
car3 = Car( "Chevette", 2010, "red", False, "car")

company = Car_company()

# company.add_car(car1)
# company.add_car(car2)
# company.add_car(car3)

# print(Car_company.car_numbers)


"""
variaveis da classe

- É compartilhada entre todas as instancias 
- Definida fora do construtor 
- Permite compartilhamento de dados entre todos os objetos da classe

"""

class Student:
    class_year = 2026
    num_students = 0
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        Student.num_students += 1
    

student1 = Student("Aluno1", 16)
student2 = Student("Aluno2", 17)
student3 = Student("Aluno3", 15)
student4 = Student("Aluno4", 15)

# print(Student.class_year)
# print(Student.num_students)

# print(f"Minha classe de graduação de {Student.class_year} terá {Student.num_students} alunos.")
# print(student1.name)
# print(student2.name)
# print(student3.name)
# print(student4.name)



"""
Inheritance = Allows a class to inherit attributes and methods from another class | class Child(parent)
"""

class Animal:
    
    classe_varialvel_teste = 100

    def __init__(self, name):
        self.name = name 
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    pass 

class Cat(Animal):
    pass


dog = Dog("Bred")
cat = Cat("Nala")

# print(cat.classe_varialvel_teste)


"""
multiple inheritance = inherit from more than one parent class
multilevel inheritance = inherit from a parent wich inherits from another parent C(B) <- B(A) <- A
"""

class Animals:

    def __init__(self, name):
        self.name = name 

    def eat(self):
        print(f"This {self.name} is eating")
    
    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animals):
    def flee(self):
        print(f"This {self.name} is fleeing") 

class Predator(Animals):
    def hunt(self):
        print(f"This {self.name} is hunting") 

class Rabbit(Prey):
    pass 

class Hawk(Predator):
    pass 

class Fish(Prey, Predator):
    pass 

rabbit = Rabbit("Pernalonga")
hawk = Hawk("Eagly")
fish = Fish("Nemo")

# fish.flee()
# fish.hunt()
# hawk.hunt()
# rabbit.flee()

# fish.sleep()

"""
A class that cannot be instantiated on its own; Meant to be subclasse. 
They can contain abstract methods, which are declared but have no implementation.
Benefits:
1. Prevents instantiation of the class itself 
2. Requires children to use inherited abstract methods 
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass 


class Car(Vehicle):

    def go(self):
        print("GO!")

    def stop(self):
        print("STOP!")

class Motorcycle(Vehicle):

    def go(self):
        print("RIDE!")
        print("You ride the bike")

    def stop(self):
        print("STOP THE BIKE!")

car = Car()

# car.go()
# car.stop()

bike = Motorcycle()

# bike.go()
# bike.stop()

"""
super() = function used in a child class to call methods from a parent class (superclass). Allows you yo extend the functionality if tge inhetited methods
"""

class Shape:
    def __init__(self, color, is_filled):
        self.color = color 
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"It is a circle with an area if {3.14 * self.radius**2}cm^2")
        super().describe()

class Square(Shape): 
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width 

    def describe(self):
        print(f"It is a square with an area if {self.width * self.width}cm")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width 
        self.height = height 

    def describe(self):
        print(f"It is a triangle with an area if {self.width * self.height / 2}cm")
        super().describe()

# circle = Circle(color="red", is_filled=True, radius=5)
# square = Square(color="blue", is_filled=False, width=6)
# triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

# triangle.describe()

"""
Polymorphism = Greek word that means to "have many forms of faces"
Poly = Many
Morque = Form

TWO WAYS TO ACHIEVE POLYMORPHISM

1. Inheritance = An object could be treated of same type as a parent class 
2. "Duck typing" = Object must have necessary attributes/methods
"""

class Shapes:
    
    @abstractmethod
    def area(self):
        pass 

class Circles(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2 

class Squares(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side  

class Triangles(Shapes):
    def __init__(self, base, height):
        self.base = base 
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
 
class Pizza(Circles):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circles(4), Squares(5), Triangles(6, 7), Pizza("pepperoni", 15)]

# for shape in shapes:
#     print(f"{shape.area():.2f}cm²") # para elevar a 2 Alt + 0178

"""
Duck typing = Another way to achieve polymorphism besides Inheritance 
Object must have the minimum necessary attributes/methods 
'If it looks like a duck and quacks like a duck, it must be a duck'
"""

class Animals:
    alive = True 

class Dogs(Animals):
    def speak(self):
        print("WOOF!")

class Cats(Animals):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False

    def speak(self):
        print("HONK!")


animals = [Dogs(), Cats(), Car()]

# for animal in animals:
#     animal.speak()

"""
Aggregation = Represents a relationship where one object (the whole) contains references to one or more INDEPEDENTS objects (the parts)
-classes are independent of one another
"""

#the whole
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def adding_books(self, book):
        self.books.append(book)
    
    def list_books(self):
        return {f"{book.title} by {book.author}" for book in self.books}

#the parts
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library("NYPL") # NYPL = new york public library

book1 = Book("The Book", "John Sturt")
book2 = Book("Loving you is a losing game", "Max James Junior")
book3 = Book("Prey", "Breanna Kane")

library.adding_books(book1)
library.adding_books(book2)
library.adding_books(book3)

# for book in library.list_books():
#     print(book)


"""
Aggregation = A relationship where one object contains references to other INDEPENDENT object "has-a" relationship
Composition = The composed object directly owns its components, which cannot exist independently "owns-a" relationship
"""

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size  

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model 
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display(self):
        return f"Marca: {self.make} Modelo: {self.model} Motor: {self.engine.horse_power}(hp) Tamanho da roda: {self.wheels[0].size}cm"

car = Car(make="Honda", model="Civic", horse_power=250, wheel_size=45)
car2 = Car(make="Toyota", model="Corolla", horse_power=200, wheel_size=45)

# print(car.display())
# print(car2.display())

"""
Nested class - A class defined within another class
Class Outer
    Class Inter

Benefits: Allows you to logically group classes that are closely related Encapsulates private details that arent relevant outsize of the outer class
keeps the namespace clean, reduces the possibility of names conflits
"""

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name 
            self.position = position
        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position) 
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company = Company("SNB")
company.add_employee("Nala", "Gerente")
company.add_employee("Bred", "RH")
company.add_employee("Scar", "Dev")

company2 = Company("VM restaurant")
company2.add_employee("Marc", "Cooker")
company2.add_employee("Brenda", "Waitress")
company2.add_employee("Kant", "Bartender")


# for employee in company.list_employees():
#     print(employee)


# for employee in company2.list_employees():
#     print(employee)

#para acessar a classe Employee fora da Company, embora nao seja muito comum: 
# employee = Company.Employee("João", "Analista")
# print(employee.get_details())
# employee = company.Employee("Maria", "Desenvolvedora")
# print(employee.get_details())

"""
Static methods = A method that belong to a class rather than any object from that class (instance) usually used for genral utility functions
Instance methods  = Best for generations on instances of the class (objects) 
Static methods = Best for utility functions that do not need acces to class data
"""

class Employee_class:

    def __init__(self, name, position):
        self.name = name 
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position

employee1 = Employee_class("Eugene", "Manager")
employee2 = Employee_class("Squidward", "Cashier")
employee3 = Employee_class("Spoogebob", "Cook")

# print(Employee_class.is_valid_position("Manager"))
# print(employee1.get_info())
# print(employee2.get_info())

# print(employee3.get_info())

"""
Class methods = Allow operations related to the class itself
Take (self) as the first parameter, which represents the class itself

Instance methods = Best for operations on instance of the class (objects)
Static methods = Best for utility functions that do not need acces to class data 
Class methods = Best for class level data or require access to the class itself
"""

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa 
        Student.add_student()
        #ou desse jeito
        #Student.count += 1
        Student.total_gpa += gpa


    #instance method 
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total of students: {cls.count}"
    
    @classmethod
    def get_Average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            average = cls.total_gpa / cls.count
            return f"Average of gpa: {average:.2f}"
    
    @classmethod
    def add_student(cls):
        cls.count += 1
    

stu1 = Student("Davih", 3.2)
stu2 = Student("Isaac", 3.6)
stu3 = Student("Maria Luisa", 3.8)

# print(Student.get_count())
# print(Student.get_Average_gpa())

"""
Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
They are authomatically called by many of Python built-in operations
They allows developers to define or customize the behavior of objects
"""

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title 
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key '{key}' not found"
        
book1 = Book("The Witcher", "Andrzej Sapkowski", 346)
book2 = Book("The Witcher 2", "Andrzej Sapkowski", 400)
book3 = Book("Algoritmos", "Aditya Y. Bhargava", 290)

# print(book1) # usa a __str__
# print(book1 == book2) # usa a __eq__
# print(book1 < book2) # usa a __lt__
# print(book1 > book2) # usa a __gt__
# print(book2 + book1) # usa a __add__
# print("Andrzej" in book3) # usa a __contains__
# print(book1["author"]) # usa a __getitem__


"""
property = Decorator used to define a method as a property (it can be accessed like a attribute)
benefits: Add addicional logit when read, write or delete attributes
gives you getter(read), setter(write) and deleter(delete) method
"""

class Retangulo:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f}cm" 

    @property
    def height(self):
        return f"{self._height:.2f}cm"  
    
    @width.setter
    def width(self, wid):
        if wid > 0:
            self._width = wid 
        else:
            f"WIdth need to be greater than 0"
    
    @height.setter
    def height(self, hei):
        if hei > 0:
            self._height = hei 
        else:
            f"Height need to be greater than 0"

    @width.deleter
    def width(self):
        del self._width
        print("Width was deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height was deleted")

    

retangulo = Retangulo(3, 4)
retangulo.width = 2

print(retangulo.width)
print(retangulo.height)

del retangulo.width
del retangulo.height

class Test:
    def __init__(self):
        pass
    def __call__(self):
        print("Invoking '__call__' method")

class AnotherTest():
    def __init__(self):
        pass
    def run(self):
        print("Invoking '__call__' method")
    __call__ = run

test = Test()
another_test = AnotherTest()

test()
another_test()