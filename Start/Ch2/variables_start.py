# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)

# Operators are used to perform operations on variables
# print("Addition:", myint + myfloat)
# print("Subtraction:", myfloat - myint)
# print("Multiplication:", myint * 2)
# print("Division:", myfloat / 3)
# print("Integer Division:", myfloat // 3)
# print("Modulus:", myint % 3)
# print("Exponentiation:", myint ** 2)


# Logical and comparison operators 
# print(myint == 10)  # equality
# print(myfloat != 5)  # inequality
# print(myint > 20)   # greater than
# print(myfloat <= 10) # less than or equal to

# print(myint > 5 or myfloat < 20)  # logical or
# print(myint < 5 and myfloat < 20)  # logical and
# print(not (myint < 5 or myfloat < 20))

# re-declaring a variable works
myint = "abc"
print(myint)