# Nested For Loop is a For Loop inside a For Loop commonly used to iterate through a multi-dimensional collection.

# Using Range in Nested For Loops
# Example 1
for x in range(5):
    for y in range(5):
        print("Hello!") 

# Example 2
for x in range(5):
    for y in range(5):
        print("Hello!",end="")
    print()

# Reading Multi-Dimentional Collections Using Nested For Loop
# Example 1
courseStudents = [
    ["BSIT","Anna"],
    ["BSIT","Aubrey"],
    ["BSIT","Rizza"],
    ["BSIT","Angel"],
    ["BSIT","Nikol"],
    ["BSIT","Sheena"]
]

for ListStudent in courseStudents:
    for i in ListStudent:
        print(i)
    print()
  
# Challenge
# Extracting the Data

students = [
    ["BSIT",["Anna","Aubrey","Rizza"]],
    ["BSCS",["Sheena","Angel","Nikol"]]
]

for student in students:
    print(student[0])
    for x in student[1]:
        print("   -" + x)
    print()
 