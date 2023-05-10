# Indentation is used to Indicate what statements are included inside for the For Loop. 

# For Loop is a statement that is commonly used to iterate through a collection or to execute a block of code in a certain amount of times. 

# For Loop in Collections (Can be used to access every item in a Collection (Lists and Tuples) in a very easy way.)
# Syntax: for x in collection # Do Something
fruits = ["Apple", "Mango", "Orange", "Grapes", "Watermelon"]
# You can read the syntax like this "For every x which is the values inside the List in fruits".
for x in fruits:
    print(x)

# Else in For Loop (Else is added to the bottom of a for loop so that it can execute code when the loop is done.)
# Syntax: for x in collections # Do Something else: # Do Something
fruits = ["Apple", "Mango", "Orange", "Grapes", "Watermelon"]

for x in fruits:
    print(x)
else:
    print("That's all!") 

# Break Keyword in For Loop (Is used to stop the loop earlier than its supposed to finish.)
fruits = ["Apple", "Mango", "Orange", "Grapes", "Watermelon"]

for x in fruits:
    print(x)
    break

# Conditions in For Loop (You can use any Conditional Statement inside a For Loop.)
# Example 1
fruits = ["Apple", "Mango", "Orange", "Grapes", "Watermelon"]

for x in fruits:
    print(x)
    if x == "Grapes":
        break

# Example 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print("This is an Even Number : " + str(number))
    else:
        print("It's an Odd Number! : " + str(number))

# Range in For Loop (A set of code in a specified number of times.)
# Syntax: for x in range(y): # Do Something 

# Example 1
for x in range(100):
    print(x)

# Example 2
for x in range (10):
    print("I miss you!")

# Account Authentication Simulation

username = ["Anna", "Marie", "AnnaMawi"]
password = ["admin123", "admin456", "admin789"]

empUsername = input("Username : ")
empPassword = input("Password : ")

for x in range(len(username)):
    if empUsername == username[x] and empPassword == password[x]:
        print("Welcome, " + username[x])
        break
else: 
    print("Account Not Found!")




