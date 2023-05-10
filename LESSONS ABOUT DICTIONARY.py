# Dictionary is a collection of key pairs that is unordered, changeable, and Indexed. 
# Notes: Keys are always Strings. 

# Ways to Access the Dictionary

# Reading the Whole Dictionary (You can read a dictionary by printing the whole dictionary.)
# Syntax: print(dictionary)
studentOne = {
    "Name" : "Anna",
    "Course" : "BSIT",
    "Age" : 20
}
studentTwo = {
    "Name" : "Marie",
    "Course" : "BSCS",
    "Age" : 21
}
print (studentOne)
print (studentTwo)

# Reading Dictionary Items (You can read a dictionary by specifying the key value.)
# Syntax: print(dictionary[key])
studentOne = {
    "Name" : "Anna",
    "Course" : "BSIT",
    "Age" : 20
}
print(studentOne["Age"])

# Reading Dictionary Items Get (You can also use Get to read a dictionary by specifying the key value.)
# Syntax: print(dictionary.get(key))
studentOne = {
    "Name" : "Anna",
    "Course" : "BSIT",
    "Age" : 20
}
print (studentOne.get("Course"))

# Assigning Dictionary Items (You can change a value of a certain item in a dictionary by specifying the key value and using the Assignment Operator "=".)
# Syntax: dictionary[key] = value
studentOne = {
    "Name" : "Marie",
    "Course" : "BSCS",
    "Age" : 21
}
studentOne ["Age"] = 20
print(studentOne.get("Age"))

# Dictionary Length (You can check the number of items (key pairs) in a Dictionary by using the len() function.)
# Syntax: len(dictionary)
studentOne = {
    "Name" : "Marie",
    "Course" : "BSCS",
    "Age" : 21
}
studentTwo = {
    "Name" : "Anna",
    "Course" : "BSIT",
    "Age" : 20
}
print(len(studentOne))
print(len(studentTwo))

# Dictionary Add Items (You can add items on a dictionary just by assigning a non-existent ket value in the dictionary.)
# Syntax: dictionary [key] = value
studentOne = {
    "Name" : "Marie",
    "Course" : "BSCS",
    "Age" : 21
}
studentOne ["Gender"] = "Female"
print (studentOne)

# Dictionary Deleting Items by Pop() (Pop() deletes an item based on their key value.)
# Syntax: dictionary.pop(key)
studentOne = {
    "Name" : "Anna",
    "Course" : "BSIT",
    "Age" : 20,
    "Gender" : "Female"
}
studentOne.pop("Age")
print (studentOne)

# Dictionary Deleting Items by POPITEM() (Deletes the last inserted item on the dictionary.)
# Syntax: dictionary.popitem()
studentOne = {
    "Name" : "Anna",
    "Course" : "BSIT",
    "Age" : 20,
    "Gender" : "Female"
}
studentOne.popitem()
print (studentOne)

# Clearing a Dictionary (Deletes all the items in a Dictionary.)
# Syntax: dictionary.clear()
studentOne = {
    "Name" : "Anna",
    "Course" : "BSIT",
    "Age" : 20,
    "Gender" : "Female"
}
studentOne.clear()
print (studentOne)

# Copying a Dictionary (Copies the whole dictionary which can be assigned to a new dictionary.)
# Syntax: student = {"Name": "Anna", "Gender"": "Female"} studentTwo = student.copy()
studentOne = {
    "Name" : "Marie",
    "Course" : "BSCS",
    "Age" : 21
}
studentTwo = {
    "Name" : "Anna",
    "Course" : "BSIT",
    "Age" : 20
}
studentThree = studentTwo.copy()
print (studentThree)

# Getting all the Keys in Dictionary (Returns a list that contains all the keys inside your dictionary.)
# Syntax: dictionary.keys()
studentOne = {
    "Name" : "Marie",
    "Course" : "BSCS",
    "Age" : 21
}
print (studentOne.keys())

# Getting all the values in Dictionary (Returns a list that contains all the value inside your dictionary.)
# Syntax: dictionary.values()
studentOne = {
    "Name" : "Marie",
    "Course" : "BSCS",
    "Age" : 21
}
print (studentOne.values())

# List of Dictionaries (Dictionaries inside a list.)
studentOne = {
    "Name" : "Marie",
    "Course" : "BSCS",
    "Age" : 21
}
studentTwo = {
    "Name" : "Anna",
    "Course" : "BSIT",
    "Age" : 20
}
students = [studentOne, studentTwo]
print (students[1].get("Course"))

# Nested Dictionaries (A Dictionary inside a Dictionary.)
studentsBMI = {
    "Height" : 150,
    "Weight" : 45,
    "Weight Status" : "Normal"
}
studentOne = {
    "Name" : "Marie",
    "Course" : "BSCS",
    "Age" : 21,
    "BMI": studentsBMI
}

print (studentOne.get("BMI"))
