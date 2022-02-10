# Overriding is the process of overriding a behaviour from a parent class.

class Animal:
    babies = 0

    def reproduce(self):
        self.babies += 1

class Dog(Animal):
    def reproduce(self):
        self.babies += 6


john = Dog()
john.reproduce()
print(john.babies)
