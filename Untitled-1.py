# Input the name from user ( Enter Name Middlename Surname)
name = input("Enter the name  Surname")

# Print the name 
print("Hello",name)


# Capitalize the first letter of name 
name =name.capitalize()
print(name)
# Capitalize the first letter of each word
name = name.title()
print(name)

# ValueError 
"""
A ValueError in Python is a type of exception that occurs
when a function receives an argument of the correct type 
but an inappropriate value.
"""
first, last = name.split()
print(f"Hello {first}")

# Integers
x = input("What's your Number?")
y = input("What's your Number?")
x = int(x)
y = int(y)
div= x/y
mul = x*y
add = x+y
sub = x-y

print(div)
print(mul)
print(add)
print(sub)

x = int(input("What's your Number?"))
y = int(input("What's your Number?"))
mod = x%y
floorDiv = x//y
add = x+y
sub = x-y
print(mod)
print(floorDiv)
print(mul)
print(add)
print(sub)
print(int(x/y))

# Find the data type

print(type(add))

# Change the data type and then confirm it by checking the datatype
addFloat = float(add)
print(type(addFloat))

# Check the data type
print(type(name))