# Overloading is not technically possible in Python without creating our own overloading class.

class Animal:
    def eat(food):
        return f"{food} eaten. Nom"

    def eat(amount, food):
        return f"{amount} {food} eaten. Nom"

#This example would not execute as we intend it to, as the first eat method is immediately overwritten by the second eat method,
# and so is now impossible to reference.

# We can achieve similar results using default arguments, however.

class Animal:
    def eat(food, amount=None):
        if amount is None:
            return f"{food} eaten. Nom."
        else:
            return f"{amount} {food} eaten. Nom."