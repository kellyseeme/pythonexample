#!/usr/bin/env python
class Animal(object):
    pass
class Dog(Animal):
    def __init__(self,name):
        self.name = name

class Cat(Animal):
    def __init__(self,name):
        self.name = name

class Person(object):
    def __init__(self,name):
        self.name = name
        self.pet = None

class Employ(Person):
    def __init(self,name,salary):
        super(Employ,self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog('Rover')
satan = Cat('satan')
mary = Person('Mary')

mary.pet = satan

frank = Employ('Frank',120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()
