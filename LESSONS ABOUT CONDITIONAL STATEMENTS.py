# Conditional Statements is a statement that makes the program smarter, it makes the program decides on what to do in ceratin CONDITIONS.

# Conditional Statements
# IF Statement (1 Condition)
# IF Else Statement (2 Conditions)
# IF ELIF ELSE Statement (3 or More Conditions)
# Nested Conditional Statements (Condition after a Condition)

# Conditional Operators
# == / Equal
# != / not Equal
# > / Greater Than 
# < / Less Than
# >= / Greater Than or Equal
# <= / Less Than or Equal

# Indentation is used to indicate what statements are included inside the Conditional Statement. 

# IF Statement (Used when dealing with One Condition.)
# Syntax: if valueOne == valueTwo: #Do Something
age = int(input("Enter Your Age : "))

if age >= 18:
    print("Legal Age")
    print("Thankyou for using the Program")

# IF Statement (Used when dealing with Two Conditions.)
# Syntax: if valueOne == valueTwo: #Do Something else: #Do Something
age = int(input("Enter Your Age : "))

if age >= 20:
    print("Legal Age")
else: 
    print("Too Young")

# IF-ELIF-ELSE Statement (Used when dealing with Three or More Statement.)
# Syntax: if valueOne == valueTwo: #Do Something elif valueOne >= valueTwo: #Do Something else: #Do Something
age = int(input("Enter Your Age : "))

if age >= 18:
    print("Legal Age")
elif age >= 13:
    print("Teenager")
else:
    print("Too Young")

# Nested Conditional Statement (Used when dealing with Conditions inside a condition.)
# Syntax: if valueOne == valueTwo: if valueThree == valueFour: #Do Something elif valueThree == valueFive: #Do Something else: #Do Something 
age = int(input("Enter Your Age :"))
height = int(input("Enter Your Height : "))

if age >= 18:
    if height >= 170:
        print("Legal Age and Tall")
    elif height >= 156:
        print("Legal Age and Average")
    else:
        print("Legal Age and Short")

# NOT Keyword (Used to invert the condition value.)
# Syntax: if not valueOne == valueTwo #Do Something
age = int(input("Enter Your Age :"))

if not age >= 18:
    print("Too Young")
else:
    print("Legal Age")

# Logical Operators (Used to include 2 or more conditions in one line.)
# Logical Operators
# AND - BOTH condition must be true.
# OR - EITHER condition must be true.

# AND STATEMENT
# Example 1
age = int(input("Enter Your Age :"))
height = int(input("Enter Your Height : "))

if age >= 18 and height >= 176:
    print("Legal Age and Tall")
elif age >= 18 and height >= 150:
    print("Legal Age and Average")
elif age >= 18:
    print("Legal Age and Short")
else: 
    print("Too Young")

# Example 2
username = input("Enter Your Username : ")
password = input("Enter Your Password : ")

if username == "Anna" and password == "admin123":
    print("Welcome Anna!")
elif username == "Marie" and password == "admin 456":
    print("Welcome Marie!")
else:
    print("Invalid Crendetials. Please try again!")

# OR STATEMENT (BOOLEAN)
# Example 1
# Teacher said that you need to bring a METERSTICK OR RULER

hasMeterStick = True
hasRuler = False

if hasMeterStick or hasRuler:
    print("You can Enter!")
else:
    print("You can't Enter!") 

# Collection Conditional Statements (Used to check an item if it's in a collection (list and tuples.))
# Syntax: list [item1,item2, item3] if value in list: #Do Something else: #Do Something
 
bag = ["wallet", "gun", "lipstick", "laptop", "earphone"]

if "gun" in bag:
    print("You can't Enter!")
else:
    print("You may proceed to the next checkpoint!")     

# Grade Average Program

gradeOne = int(input("Grade for OLCC04 : "))
gradeTwo = int(input("Grade for OLPT01 : "))
gradeThree = int(input("Grade for OLHCI1 : "))

average = (gradeOne + gradeTwo + gradeThree) / 3
print("Average : " + str(average))

if average > 100 or average <= 50:
    print("Invalid Grade")
elif average >= 98:
    print("With Highest Honors")
elif average >= 95:
    print("With High Honors")
elif average >= 90:
    print("With Honors")
elif average >= 75: 
    print("Passed")
else:
    print("Failed")

