# create class called budget and enter the attributes: self, food, clothing, entertainment
# create a way for these objects to allow depositing and withdrawing funds (method) inside class

class Budget:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


# setting the balance for each category
food = Budget(50)
clothing = Budget(20)
entertainment = Budget(70)
pets = Budget(12)

# this goes into the withdraw method within the class and takes away the amount specified
food.withdraw(10)
clothing.withdraw(20)
entertainment.withdraw(50)
pets.withdraw(10)

print("Food balance:", food.balance)
print("Clothing balance:", clothing.balance)
print("Entertainment balance:", entertainment.balance)
print("Pet balance", pets.balance)

# this goes into the deposit method within the class and adds the amount specified
food.deposit(20)
clothing.deposit(10)
entertainment.deposit(100)
pets.deposit(8)

print("Food balance:", food.balance)
print("Clothing balance:", clothing.balance)
print("Entertainment balance:", entertainment.balance)
print("Pet balance", pets.balance)