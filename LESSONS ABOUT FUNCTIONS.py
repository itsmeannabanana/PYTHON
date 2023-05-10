# Functions are used to organize and divide specific tasks in a program that will only run when it is called. 

# Indentation is used to indicate what statements are included inside a function. 

# Creating Function
# Syntax: def.function_name(); #Do Something 
def sayHello():
    print("Hello!")

# Calling a Function
# Syntax: def.function_name(); #Do Something function_name()
def sayHello():
    print("Hello!") 
sayHello()

# Arguments or Parameters are values passed inside a Function that will be used to perform tasks. 
# Syntax: def function_name(parameters): #Do Something  function_name(parameter)
# Example 1
def sayHello(firstname):
    print("Hello, " + firstname)
sayHello("Anna!") 

# Example 2
def sayHello(firstname):
    print("Hello, " + firstname)
name = input("Enter Name")
sayHello(name) 

# Example 3
def sayHello(firstname,lastname):
    print("Hello, " + firstname + " " + lastname)
sayHello("Anna", "Olavides")

# Return Values is a value returned after a Frunction is done executing it is used to get results from a function that computes or does something that needs a result. 
# Syntax: def function_name(parameters) return value function_name(paramater)
# Example 1
def add(numOne,numTwo):
    return numOne + numTwo
sum = add(10,10) 
print(sum) 

# Example 2
def subtract(numOne,numTwo):
    return numOne - numTwo
difference = subtract(10,10) 
print(difference)   

# Example 3
def isLegalAge(age):
    if age >= 18:
        return True
    else:
        return False
print(isLegalAge(17))

# Challenge
# Square a Number using Functions with Parameters
number = int(input("Number : "))

def square(number):
    return number * number
int = square(number)
print(int)
