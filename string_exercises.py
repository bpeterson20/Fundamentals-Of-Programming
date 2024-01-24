# getting user input
user_input = input("Give me a string bozo?\n")
print(user_input)
# getting total length of string
length = len(user_input)
# getting middle character and rounding up
middle_Pos = int(length / 2)  # need to convert to int because indices should always be integers

# first character
first_char = user_input[0]
# last character
last_char = user_input[-1]
# middle character
middle_char = user_input[middle_Pos]

print(first_char, middle_char, last_char)
