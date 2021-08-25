'''
Module 4 - Functions, Tuples, Dictionaries, and Data Processing

    1) Writing functions in Python
    2) Returning a result from a function
    3) Scopes in Python
    4) functions

'''
'''Function's
Are some instruction pack together that perform's a specific task
'''
def function_1():
    print("Function one")

print("======"*10)
function_1() # calling  a function { () <- this executes a function }
function_1 #  not executed

# return statment
def return_functions():
    return True
print("======"*10)
obj_1 = return_functions() # function executed (A function can also be assigned to a variable (FIRST CLASS FUNCTIONS))
print(obj_1)
print("======"*10)
# with parameters and arguments , default arguments and *arguments , **keywordarguments

def parameters(para_1,para_2):
    return f'{para_1} .... {para_2} '

print(parameters(True,False))
print("======"*10)

def default_para(dob ,name='mohammed mouizuddin'):
    return f'I am {name} and my year of birth is {dob} '
print(default_para(1998))
print("======"*10)

# *arguments , **keywordarguments, allows to have arbitrary number of positional arguments or key word argumentgs
def function_2(*arg,**kwargs):
    print(arg) # args gives a tuple
    print( kwargs)  # kwargs will give a dictionary

function_2(1,2,3,4,5,6,7,8,9, name='NAME',city="CITY",country='INDIA')

# packing and unpacking
tuple_1 = (1,2,3,4,5,6,7,8,9)
dict_1 = dict(name='NAME',city="CITY",country='INDIA')
print("======"*10)
function_2(*tuple_1,**dict_1)
print("======"*10)
#
