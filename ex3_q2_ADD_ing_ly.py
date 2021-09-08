# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:05:26 2021

@author: kalai
"""

# Q2: For a string of length greater than or equal to 3, 
# write a Python program to add 'ing' at the end of a given string. 
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.

i_string  = input('Enter a string: ')
if len(i_string)>= 3:
    if i_string[-3:]=='ing':
        print(i_string+'ly')
    else:
        print(i_string+'ing')