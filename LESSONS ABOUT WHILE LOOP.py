# Indentation is used to indicate what statements are included inside the While Loop.

# While Loop (Is a statement that will repeat a block of code as long as its condition is fulfilled.)
# Syntax: while valOne > valTwo # Do Something
age = 12

while age < 18: 
    print ("Still Young : " + str(age))
    age = age + 1
 
# Else in While Loop (Else is added to the bottom of a while loop so that it can execute code when the loop is done.)
# Syntax: while valOne > valTwo # Do Something else: # Do Something  
age = 1

while age < 18:
    print ("Still Young : " + str(age))
    age = age + 1
else:
    print ("Legal Age : " + str(age))

# While Loop in Collections (While Loop can be used to access every item in a Collection (Lists and Tuples) since it is Indexed and Ordered.)
# Example 1

studentID = [202100451, 202100452, 202100453, 202100454]
i = 0

while i < 4:
    print (studentID[i])
    i = i + 1

# Example 2

studentID = [202100451, 202100452, 202100453, 202100454,202100455]
i = 0

while i < len(studentID):
    print (studentID[i])
    i = i + 1

# Break Keyword in While Loop (Is used to stop the loop no matter what the condition is. )
# Example 

while True:
    print ("Hello Anna!")
    break

# Conditions in While Loop (You can use any Conditional Statement inside a While Loop.)
# Example 1 

print ("Kumain ka na ba?")

while True:
    answer = input("Answer : ")
    if answer == "Yes":
        print ("Mabuti!")
        break
    else:   
        print  ("Edi kumain ka na!")

# Example 2 (You want to sort the Odd and Even Numbers)
# Notes 1. Use Modulo which is %

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0

while i < len(numbers):
    if (numbers[i] % 2 == 0):
        print ("Even Number : " + str(numbers[i]))
    else:
        print ("Odd Number : " + str(numbers[i]))
    i = i + 1
    
# Math Quiz Game
lives = 3
correctanswer = 40
correctanswer1 = 100

while lives > 0:
    answer = int(input ("20 + 20 = "))
    if answer == correctanswer:
        print ("Congratulations, you won!")
        break
    else:
        lives = lives - 1
else:
    print ("You lose, better luck next time!")
    
while lives > 0:
    answer = int(input ("60 + 40 = "))
    if answer == correctanswer1:
        print ("Congratulations, you won!")
        break
    else:
        lives = lives - 1
else:
    print ("You lose, better luck next time!")   