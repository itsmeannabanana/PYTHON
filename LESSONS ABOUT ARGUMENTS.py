# Arguments or Parameters are values passed inside a Function that will be used to perform tasks. 

# Arbitrary Arguments (*args) are used if you don't exactly know how many arguments is needed in your functions.
# PS: Arbitrary Arguments that is passed in will be considered as a tuple allowing it to be iterated using a loop.
# Syntax: def function_name(*parameter): #Do Something function_name(v1,v2,v3...)
# Example 
def sayHello(*names):
    for name in names:
        print("Hello, " + name)
sayHello("Anna", "Aubrey", "Rizza", "Sheena", "Angel", "Nikol")

# Keyword Arguments (kwargs) is an alternative way for sending arguments inside a function by specifying the parameter name in no certain order. 
# Often used in combination with Arbitrary Arguments or if you don't know the order of the arguments in the function.
# Syntax: def function_name(*p1,p2): #Do Something function_name(v1,v2, p2 = v3)
# Example 1
def sayHello(firstName,lastName):
    print(firstName + " " + lastName)
sayHello(lastName="Olavides", firstName="Anna Marie")

# Example 2
def printFamily(*firstNames, lastName):
    for name in firstNames:
        print(name + " " +  lastName)
printFamily("Anna", "Marie", "Lits", lastName="Olavides")

# Arbitrary Keywords Arguments (**kwargs) used when you are uncertain on what parameter name you want to pass.
# Syntax: def function_name(**parameter): #Do Something function_name(kword = v1, kword = v2)
# Example
def printStudent(**student):
    print(student["name"])
    print(student["course"])
    print(student["age"])
printStudent(name="Anna", age="20", course="BSIT", studentnumber="CA202100451")

# Challenge
# Summation Program
def summationof(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
print(summationof(10,10,10,10,10,10,10,10,10,10))
