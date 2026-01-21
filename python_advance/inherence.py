class Eletronic:
    def __init__(self, valor):
        self.valor = valor 

    def vender(self):
        print("Vendido")


class Celular(Eletronic):
    def __init__(self, valor, marca):
        super().__init__(valor)
        self.marca = marca
    
    def vender(self):
        super().vender()
        print("Iphone vendido")


iphone = Celular(2000, "iphone")

iphone.vender()

class Animal:
    def __init__(self, habitad):
        self.animal_habitad = habitad
    
    def habitad(self):
        print(f"My habitad is: {self.animal_habitad}")

    def sound(self):
        print("Sound")


class Dog(Animal):
    def __init__(self, habitad):
        super().__init__(habitad)
    
    def sound(self):
        print("Woof woof")    

max = Dog("quintal")
max.habitad()
max.sound()

#Multiple Inherence

class Father:
    def gardening(self):
        print("I enjoy gardening")
    
class Mother:
    def cooking(self):
        print("I love cooking")

class Child(Father, Mother):
    def sports(self):
        print("I love sports")


c = Child()
c.cooking()
c.gardening()
c.sports()


class Father:
    def skills(self):
        print("gardening, programming")
    
class Mother:
    def skills(self):
        print("cooking, art")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")


c = Child()
c.skills()