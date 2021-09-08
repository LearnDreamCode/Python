# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 06:04:47 2021

@author: kalai
"""

#Function object

#my_print is a function object that points to print function
# my_print = print

# print('Hello world from print')
# my_print('Hello world from my_print')
# print(my_print)
# my_print(print)

# iterable - list, set, dict, tuple
import math
num_list = [n**2 for n in range(10)]

# map will iterate with each element

print(list(map(math.sqrt,num_list)))

# the above map does the same with map function
# sqrt_list = list()
# for num in num_list:
#     sqrt_list.append(math.sqrt(num))

