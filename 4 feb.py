#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1. Create a python program to sort the given list of tuples based on integer value using a
#lambda function.
# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
# Sorting the list based on the integer value (runs) using a lambda function
# Given list of tuples
player_runs = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# Sorting the list based on the integer value (runs) using a lambda function
sorted_players = sorted(player_runs, key=lambda x: x[1])

# Print the sorted list
for player in sorted_players:
    print(player)

'''Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''

r=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l=list(map(lambda x:x**2,r ))
print(l)


'''Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and
lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')'''

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r=tuple(map(lambda x:str(x),l))

print(r)


'''Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.'''
from functools import reduce
l=[]
for i in range (1,26):
    l.append(i)

r=reduce(lambda x,y:x*y,l)
print(r)

'''Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
filter function.
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]'''

l=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

r=list(filter(lambda x:x%2==0 and x%3==0,l))
print(r)
'''Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
function.
['python', 'php', 'aba', 'radar', 'level']'''

l=['python', 'php', 'aba', 'radar', 'level']
# Given list of strings
strings_list = ['python', 'php', 'aba', 'radar', 'level']

# Use filter and lambda to find palindromes
palindromes = list(filter(lambda s: s == s[::-1], strings_list))

# Print the result
print("Palindromes in the list:", palindromes)


# In[ ]:




