# Do not use reserved keywords for variable name
"""
print('Hello World')
print(help('keywords'))

# try to avoid multiple variable declaration simultaneously
a = b = c = 10 # shortcut for below
a = 10
b = 10
c = 10

print(a, b, c)


# statement vs Expression
x = 47  # statement
y = x + 10  # expression


# TYPE CONVERSION --> to change the data type of a variable
# Convert float and numeric strings to int
print(int("20"))
print("30")
print(type(int("20")))

print(int(14.21))
# print(int("20.24")) # errors out because int expects only whole number inside
print(int(float("20.24")))


# STRINGS
# 3 ways to create a string - using either single, double, triple quotes
first_name = 'Jane'
last_name = "Doe"
address = "10 Main St."

job = "Physician's Assistant" # recommended to use double quotes for strings

# String Functions
# len() -> returns the number of characters in a string
print(len("Hello"))

# upper and lower --> converts the string to appropriate case
print("Hello".upper())

# string concatenation - adding up strings
first_name = "Jane"
last_name = "Doe"
age = 20

print(first_name + ' ' + last_name + ': ' + str(age))

# string multiplication - can multiple a string wit an int
print("Hello"*3)
"""
# Accessing string characters - a string is just a sequence of characters

name = "Jane Doe"
print(name[2])
# print(name[8])# throw index out of bound error

# retrieving the character at given index

print(name.index('o'))# return 6
print(name.index("e"))# returns the index of first occurrence
