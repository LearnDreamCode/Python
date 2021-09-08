# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:12:37 2021

@author: kalai
"""

# Q3: Write a Python program to display a number 
# in left, right and center aligned of width 10

i_number = int(input('Eenter a number : '))

print(str(i_number).center(10))
print(str(i_number).ljust(10))
print(str(i_number).rjust(10))