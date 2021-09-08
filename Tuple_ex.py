# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 06:36:30 2021

@author: kalai
"""

# demo creation of tuples

# similar to list but are immutable
# tuple less memory than list
# accessing an item in tuple is much much faster than its list counter part
# but if you have lots of inserts and deletes then use list
# indexing and slicing are similar to list
# things to keep in mind
# if you want to create a tuple of one item then end it with ,

t_fruits=('JackFruit','Mango','Banana','Apple','Mango')

print(t_fruits.count('Mango'))

print(t_fruits[:3])

print(t_fruits.index('Mango',2))

print(len(t_fruits))

t_num=(1)
print(type(t_num))

t_num=(1,)
print(type(t_num))