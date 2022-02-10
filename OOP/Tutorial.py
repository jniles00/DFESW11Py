from abc import ABC, abstractclassmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractclassmethod
    def eat(self):
        pass

    extinct = False


class Owl(Bird):                # this is an example of Inheritance as the Owl child class has inherited from the Bird parent class
    def reproduce(self):        # this is an example of Polymorphism as the reproduce method has been overridden
        self.babies += 6

    def eat(self):
        return "Peck peck"


class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom Nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1