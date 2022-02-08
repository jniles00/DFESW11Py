# books = {"The Handmaiden's Tale" : "Margaret Atwood", "The Hobbit": "J.R.R. Tolkein", "Charlie and the Chocolate Factory" : "Roald Dahl"}

# print(books)

# print(books["The Hobbit"])


# # Finding when Plato was born

# dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

# answer_1= -427

# print(answer_1)



# # Changing the birth year of Plato from 427 to 428

# dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}


# dict["born"] = -428

# print(dict["born"])



# # Dictionaries can have nested data too. Also, you can add a new key to a dictionary as they are mutable (changeable). 


# dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

# # nested data
# dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]

# print(dict)


# # Performing addition on a key in a dictionary

# dict={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}

# dict["son's height"] = dict["son's height"] + 2
# print(dict)

# generates a list of tuples consisting of each key value pair

dict={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}

#Type your answer below.
ans_1= dict.items()

print(ans_1)

# Using .get() method to print the value of "son's eyes"
dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}

ans_1= dict.get("son's eye color")

print (ans_1)


# using get method to get a son's age but if nothing comes up then it will return the value 2
dict={"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}

ans_1= dict.get("son's age", 2)

print(ans_1)