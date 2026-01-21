
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 

    def introduzir(self):
        return f"Ola me chamo: {self.nome}, tenho {self.idade} anos."

vitoria = Pessoa("Vitória", 22)

# introducao = vitoria.introduzir()
# print(introducao)

#####


class Student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age 
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade 


class Course: 
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True 
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)



s1 = Student('Tim', 19, 95)
s2 =  Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
# print(course.students[0].name)
#print(course.get_average_grade())

#Herança


class Pet: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know what to say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color 
    
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

# p = Pet("Tim", 19)
# p.show()
# p.speak()
# c = Cat("Bill", 34, "Orange")
# c.show()
# c.speak()
# d = Dog("Jill", 25)
# d.show()
# d.speak()
# f = Fish("Bubbles", 10)
# f.speak()

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name 
        Person.add_person()
    
    @classmethod
    def number_people(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

# p1 = Person("tim")
# print(p1.number_of_people)
# p2 = Person("jill")
# print(p2.number_of_people)
# print(Person.number_people())

# Person.add_person()
# print(Person.number_people())

# Person.number_of_people += 1
# print(p1.number_of_people)
# p1.number_of_people += 1
# print(p1.number_of_people)
# print(Person.number_of_people)
# print(p2.number_of_people)


class Math:

    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("Run")

print(Math.add5(5))
print(Math.add10(5))
Math.pr()