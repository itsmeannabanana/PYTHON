# Sets is a collection of variables that is partially writable and its unordered and unindexed.
# Notes: Hindi puwede magdagdag pero hindi mag-edit.

# Reading Whole Sets (You can read a set by printing the whole set.)
evenNumbers = {2, 4, 6, 8, 10}
print (evenNumbers)

# Set Length (You can check the number of items in a set by using the len() function.)
evenNumbers = {2, 4, 6, 8, 10}
print (len(evenNumbers))

# Set Add Items by Add() (Adds an item at the end of the set.)
evenNumbers = {2, 4, 6, 8, 10, 12, 14, 16}
evenNumbers.add (18)
print (evenNumbers)

# Set Add Items by Update() (Allows multiple items to be added at the same time in the set.)
oddNumbers = {1, 3, 5, 7, 9, 11, 13, 15}
oddNumbers.update ([17, 19, 21, 23, 25])
print (oddNumbers)

# Set Deleting Items by Remove() (Deletes an item based on their value.)
# Notes: If the value doesn't exist in the set it will be counted as an error.
evenNumbers = {2, 4, 6, 8, 10, 12, 14}
evenNumbers.remove (6)
print (evenNumbers)

# Set Deleting Items by Discard() (Deletes an item based on their value.)
evenNumbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
evenNumbers.discard (12)
print (evenNumbers)

# Set Deleting Items by Pop () (Deletes the first item in the set.)
evenNumbers = {2, 4, 6, 8, 10}
evenNumbers.pop ()
print (evenNumbers)

# Clearing a Set (Deletes all the value in a set.)
oddNumbers = {1, 3, 5, 7, 9, 11, 13, 15}
oddNumbers.clear ()
print (oddNumbers)

# Copying a Set (Copies the whole set which can be assigned to a new set.)
course = {"BSIT", "BSCS", "BLIS", "BSMT", "BSBA"}
courseList = course.copy ()
print (courseList)

# Union Set (Returns a set containing all the values of the two sets.)
courses = {"BSIT", "BSCS", "BLIS", "BSMT", "BSBA"}
foods = {"Burger", "Sundae", "Fries", "Coke"}
coursesFoods = foods.union (courses)
print (coursesFoods)

# Difference Set (Returns a set containing the values that only exists on the left set and not on the right set.)
setOne = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
setTwo = {2, 4, 6, 8, 10}
setThree = setOne.difference (setTwo)
print (setThree)

# Intersection Set (Returns a set containing the value that exists both on the two sets.)
coursesOne = {"BSIT", "BSCS", "BLIS", "BSMT", "BSBA"}
coursesTwo = {"BSIT", "BSCS", "BLIS", "BSED", "BSFM", "BSMT", "BSBA"}
coursesThree = coursesOne.intersection (coursesTwo)
print (coursesThree)

# Symmetic Difference Set (Returns a set containing all the values that exists exclusively on each set.)
setOne = {1, 2, 3, 4, 5}
setTwo = {2, 4, 6, 8, 10}
setThree = setTwo.symmetric_difference (setOne)
print (setThree)

# Disjoint Set (Returns a boolean whether two sets have an intersection or not.)
courses = {"BSIT", "BSCS", "BLIS", "BSMT", "BSBA"}
foods = {"Burger", "Sundae", "Fries", "Coke"}
print (courses.isdisjoint(foods))

# Subset (Returns a boolean whether the left set contained in the right set.)
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
oddNumbers = {1, 3, 5, 7, 8, 9}
print (oddNumbers.issubset(numbers))

# Superset (Returns a boolean whether the right set is contained in the left set.)
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
evenNumbers = {2, 4, 6, 8, 10}
print (numbers.issuperset(oddNumbers))

# Casting Sets (You can cast sets to Tuple or List and ViceVersa in the same way you cast other variables.)
