# Abstraction allows us to create the lowest level blueprint of a class 
# without anyone being able to create an instance of that class.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod # stops other classes from creating instances of this method
    def eat(self):
        pass

class Mammal(Animal):
    def eat(self):
        return "Nom Nom"