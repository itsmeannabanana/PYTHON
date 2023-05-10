# List is a read and write collection of variables that maybe used to start certain data. 

# Reading List Items (Reading a list by printing of the items inside it by using an index.)
# print (list[index])

# Assigning List Items (Assigning a list item by using an index Assignment Operator)
courses = ["BSIT", "BSCS", "BLIS", "BSMT", "BSBA"]
courses = "BSMT"
print (courses)

# List Length (Checking the number of items in a list.)
courses = ["BSIT", "BSCS", "BLIS", "BSMT", "BSBA"]
print (len(courses))
 
# List Count (Counting how many times an item occurs in a list.)
courses = ["BSIT", "BSCS", "BLIS", "BSCS", "BSCS", "BSIT"]
print (courses.count("BSCS"))

# List Add Items by Appened() (Adds an item at the end of the list.)
courses = ["BSIT", "BSCS", "BLIS"]
courses.append ("BSMT")
print (courses)

# List Add Item by Insert() (Adds an item at the specified index.)
courses = ["BSIT", "BSCS", "BLIS"]
courses.insert (1, "BSMT")
print (courses)

# List Deleting Items by Pop() (Deletes an item based on their index and if index is not specified it deletes the last item.)
courses = ["BSIT", "BSCS", "BLIS"]
courses.pop (0)
print (courses)

# List Deleting Items by DEL (Deletes an item based on their index and if index is not specified it deletes the whole list.)
courses = ["BSIT", "BSCS", "BLIS"]
del courses [1]
print (courses)

# Clearing a List (Deletes all the value in a list.)
courses = ["BSIT", "BSCS", "BLIS"]
courses.clear ()
print (courses)

# Copying a List (Copies the whole list which can be assigned to a new list.)
courses = ["BSIT", "BSCS", "BLIS", "BSMT", "BSBA"]
y = courses.copy ()
print (y)

# Combining List by Adding (You can use "+" operator to combine list.)
# Two Examples
courses = ["BSIT", "BSCS", "BLIS", "BSBA", "BSMT"]
strand = ["ABM", "STEM", "ICT", "SMAW", "HUMMS"]
print (courses + strand)

courses = ["BSIT", "BSCS", "BLIS", "BSBA", "BSMT"]
strand = ["ABM", "STEM", "ICT", "SMAW", "HUMMS"]
coursesStrand = courses + strand 
print (coursesStrand)

# Combining List by Extend() (Combines list by appending the specified list to the end of the first list.)
courses = ["BSIT", "BSCS", "BLIS", "BSBA", "BSMT"]
strand = ["ABM", "STEM", "ICT", "SMAW", "HUMMS"]
courses.append (strand)
print (courses)

# Reverse List Item (Reverses the order of the List's Items.)
strand = ["ABM", "STEM", "ICT", "SMAW", "HUMMS"]
strand.reverse ()
print (strand)

# Sort List Items (Sorts list items by Alphabet or Value depending on the datatype.)
# Two Examples (Ascending and Descending)

ascending = ["BSIT", "1", "BSCS", "2", "BSCS", "3"]
ascending.sort ()
print (ascending)

descending = ["BSIT", "1", "BSCS", "2", "BSCS", "3"]
descending.sort (reverse = True)
print (descending)

# Nested List (A list inside a list known as sublist.)
courses = ["BSIT", "BSCS", "BLIS", "BSBA", "BSMT", ["ICT", "ABM", "STEM"]]
print = (courses[3][1])