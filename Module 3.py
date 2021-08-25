'''Module 3 - Boolean Values, Conditional Execution, Loops, Lists and List Processing, Logical and Bitwise Operations

    1) Conditions
    2) Python's loops
    3) Logic and bit operations in Python
    4) Collections in python (List ,tuple,set and dictionaries)

'''
#  1) Conditions
'''
What statment gets executed,depending on whether a certain value are TRUE or FALSE
boolean True
boolean False
'''
condition = True
# condition statment will only execute if the statment is true
if True:
    print(True) # will execute since if condition is true
else:
    print(False)

pro_lan = 'Python'.lower()
if pro_lan == 'java':
    print(f'Statment I')
elif pro_lan == 'python':
    print(f'Statment II')
else:
    print("This statment will run if none of the condtions are true")

print("======="*10)

# and ,or ,not

user = 'Admin'.lower()
log_in = True

if user == 'admin' and  log_in: # and if both condition are true then the statment is true
    print("Admin page")
else:
    print('User Dashboard')

if user == 'user' or  log_in: # and if any one  condition is true  then the statment is true
    print("Admin page")
else:
    print('User Dashboard')

print(not True)
print(not False)

print("======="*10)

#  2) Python's loops
'''
for loop (finite loops) 
while loop (infinite loops)
'''
for i in range(10): # start with 0 by deafult , stop(exclusive) ,step
    print(i)

lists = 'a b c d e f'.split() # this split() method converts string to list
for i in  lists:
    print(i,end=" ")

# break , continue
'''
break : break's the loop
continue : continue's the loop without breaking
'''
for i in range(1, 10 + 1):
        if i % 2 == 0:
            print(f'enevs {i}')
            continue # this will continue without breaking/ending loop
        else:
            print(f'oods  {i}')
        # print(i)
# break
for i in range(10):
    if i == 5:
        print(f"Breaking from loop.... \nfound {i}")
        break # this will break the loop
    print(i)

# mainly break statment are used to break infinite loops (while loops)

while True : # this will be an infinite loop if there no Termination
    user_input = input("Enter 1 or quit to Termination  else continue")
    if user_input == '1' or user_input == 'quit':
        break

#  4) Collections in python (List ,tuple,set and dictionaries)
'''List - []
1) Lists are ordered
2) Lists are mutable / changeable
3) Lists are dynamic
'''

# empty lists
empty_list_one = list()
empty_list_two = []
print("======="*10)
# Lists
programming_languages = ['Python','Java', 'C','C++','Rust'] # list of programming languages
print(programming_languages)
print("======="*10)
# Array slicing [start (inclusive) : stop (exclusive) : stept ]

programming_languages[0]
programming_languages[0:4]
programming_languages[::1]
programming_languages[-1]
print(programming_languages)

print("======="*10)
# Lists are mutable / changeable
print(programming_languages[0])
programming_languages[0] = 'Python is easy to code/learn/practice'
print(programming_languages[0])
print("=="*10)
# list method :
for list_methods in dir(list):
    if list_methods[0]!="_":
        print(list_methods)
'''
append
clear
copy
count
extend
index
insert
pop
remove
reverse
sort
'''

programming_languages.append('Java Script') # append : add's a element at the end of the list
# programming_languages.clear() # copy() method copies the list and returns the copied list.
new_list = programming_languages.copy()
programming_languages.count('Python') # returns the count of how many times a given object occurs in a List.
new_list = ['Ruby','C#']
programming_languages.extend(new_list) # extend() is a built-in function that adds the specified list elements (or any iterable) to the end of the current list
programming_languages.index('Java') # index() method returns the index of the given element in the list.
programming_languages.pop() # removes this method vthe last element
programming_languages.remove('Java') # this method removes sprcific element
programming_languages.reverse() # this method reverses the list
programming_languages.sort() # this method can be used to sort a list in ascending, descending or user defined order
print(programming_languages)
print("======="*10)
# Tuple
'''Tuple - ()
1) Tuple are ordered
2) Tuple are immutable / unchangeable
'''
# empty Tuple
empty_tuple_one = tuple()
empty_tuple_two = ()

tuple_example = (1001,1001,1001,1002,1003,1004,1005,) # sample ID's
for tuples_methods in dir(tuple):
    if tuples_methods[0] != "_":
        print(tuples_methods)

'''Tuples methods
count
index
'''
tuple_example.count(1001) # this method count the frequency of an element in a tuple
tuple_example.index(1001) # this method searches for the given element in a tuple and returns its position. It returns first occurrence of the element in the tuple

'''Note
If you need something that,you can modify then use a list
if you need to just loop through ,access ,store elements which you don't want to modify if then use a tuple
'''

'''dictionaries
are key value pairs 
key : are unique values
value : are the data associated to keys
'''
dictionary = {"key-1": [1,2,3,3,4] , "key-2": (1,2,3,4)}
details = {'name': 'NAMWE', 'batch': 'BATCH', 'university':'UNIVERSITY'}
print(details)
details.update({'name':'TEST_01', 'batch':'2017-2021'}) # update method : updates multiple keys in a dictionary
print(details)
#  looping over a dictionary
for to_loop in details: # this will only loop over keys
    print(to_loop)

for key,value  in details.items():
    print(f'dictionary keys are {key}')
    print(f'dictionary values are {value}')

'''For more methods in dictionaries
for dictionaries_methods in dir(tuple):
    if dictionaries_methods[0] != "_":
        print(dictionaries_methods)
'''