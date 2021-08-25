print('\t Module 2 - Data Types, Variables, Basic Input-Output Operations, Basic Operators  \n ')

'''Module 2 - Data Types, Variables, Basic Input-Output Operations, Basic Operators

    1) Your first program
    2) Python literals
    3) Operators - data manipulation tools
    4) Variables - data-shaped boxes
    5) How to talk to computer?
'''

# 1) Your first program :
# print("Your first program in python")


''' 2) Python literals
2.1. String literals
2.2. Numeric literals
2.3. Boolean literals
2.4. Special literals
'''
# 2.1 String literals :
string_literals = "String literals in python"
print(string_literals)
# methods
upper_case = string_literals.upper()
lower_case = string_literals.lower()
capitalize = string_literals.capitalize()
count_char = string_literals.count('String')
find_char = string_literals.find('python')
# replace_char = string_literals.replace('String','Strings')
print(dir(string_literals)) # all methods associated to a string

# indexing
indexing_1 = string_literals[:]
indexing_2 = string_literals[0:10] # [start,end]  [stat : Including , end : excluding ]
indexing_3 = string_literals[0::2] # [start,end,stepts]
print(indexing_3) # String
reversing_string = string_literals[::-1]


#  2.2. Numeric literals

numeric_literals = 1078
numeric_literals.conjugate()
print(dir(numeric_literals))

print(abs(-100))
print(round(22/7,2))

# 2.3. Boolean literals : TRUE / FALSE

print(1==1)
print(1==100)

# 2.4. Special literals : NONE
# None is used to specify to that field that is not created. It is also used for the end of lists in Python.
var_1 = None
print(var_1)
var_1 = "Value assigned as string"
print(var_1)

# 3) Operators - data manipulation tools
'''
3.1 Arithmetic operators
3.2 Comparison operators
3.3 Assignment Operators
3.4 Logical Operators
3.5 Membership Operators
3.6 Identity Operators
'''
# 3.1 Arithmetic operators
# The operator can be defined as a symbol which is responsible for a particular operation between two operands

print( 1 + 1)  # Addition
print( 11 - 1)  # Subtraction
print( 11 * 11) # Multiplication
print( 10 / 5)  # divide
print( 3 // 2)  # floor division
print( 3 ** 3)  # Exponent

# 3.2 Comparison operator
# Comparison operators are used to comparing the value of the two operands and returns Boolean true or false accordingly.

print( 10 == 1) # If the value of two operands is equal, then the condition becomes true.
print( 10 != 1) # If the value of two operands is not equal, then the condition becomes true.
print( 10 > 1)          # If the first operand is greater than the second operand, then the condition becomes true.
print( 10 < 1)  # If the first operand is less than the second operand, then the condition becomes true.
print( 10 >= 1) # If the first operand is greater than or equal to the second operand, then the condition becomes true.
print( 10 <= 1) # If the first operand is less than or equal to the second operand, then the condition becomes true.

# 3.3  Assignment Operators
# The assignment operators are used to assign the value of the right expression to the left operand.

variable = 1078  # It assigns the value of the right expression to the left operand.
print(variable)
variable += 10 # It increases the value of the left operand by the value of the right operand and assigns the modified value back to left operand.
print(variable) # 1078 + 10 = 1080
''' 
same logic goes to 
-= , *= , /= , //= , %= **=
'''
# 3.4 Logical Operators
# The logical operators are used primarily in the expression evaluation to make a decision
print( True and True) # and { If both the expression are true, then the condition will be true }
print(True or True) # or { If one of the expressions is true, then the condition will be true }
print(not False) # If an expression a is true, then not (a) will be false and vice versa

# 3.5 Membership Operators
# Python membership operators are used to check the membership of value inside a Python data structure (list,tuples,dict)
membership_operators = [1,2,3,4,5,6,7,8,9,10]
print(1 in membership_operators)# It is evaluated to be true if the first operand is found in the second operand (list, tuple, or dictionary).
print(1 not in membership_operators) # It is evaluated to be true if the first operand is not found in the second operand (list, tuple, or dictionary).

# 3.6 Identity Operators
# The identity operators are used to decide whether an element certain class or type
id_1 = "string_1"
id_2 = 'string_2'
print(id(id_1))
print(id(id_2))
# It is evaluated to be true if the reference present at both sides do not point to the same object
print(id_1 is not id_2)

#  4) Variables - data-shaped boxes
# Variables are used to store information to be referenced and manipulated in a computer program
name_variable = "name" # name variable
int_variable = 1078 # int variable
float_variable = 3.14