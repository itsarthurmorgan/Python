import re

# ask the user for an algebraic expression
expression = input("Enter an algebraic expression: ")

# use a regular expression to find all instances of a number followed by a variable
pattern = r'(\d)([a-zA-Z])'

# replace each instance with the number and variable separated by a multiplication symbol
expression = re.sub(pattern, r'\1*\2', expression)

# print the modified expression
print(f"Modified expression: {expression}")
