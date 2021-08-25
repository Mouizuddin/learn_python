'''
Module 1 - Introduction to Python and Computer Programming

    1) Python - a tool, not a reptile :)
    2) There is more than one Python
    3) Let's start our Python adventur

'''
# first code in python

# print('Learn Python')
# list and tuples
count = 0
for ii in dir(list):
    if ii[0] !="_":
        count += 1
        # print(ii)
print('total number of list ,methods >> {}'.format(count))
''' append
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
list_test = [1,2,3,4,5,6,7,8,9,10]
new_list = [11,13,89,12,90,15,17,16]
list_test.clear()
list_test.extend(new_list)
list_test.pop(2)
list_test.sort()
list_test.reverse()
print(list_test)
