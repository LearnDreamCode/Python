# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 06:03:01 2021

@author: kalai
"""

greetings = 'very good morning'

# print('As is          :',greetings)
# print('upper          :',greetings.upper())
# print('lower          :',greetings.lower())
# print('title          :',greetings.title())
# print('capitalize     :',greetings.capitalize())
# print('swapcase       :',greetings.swapcase())

input_string = input('Enter your name: ').casefold()
if input_string == 'tom'.casefold():
    print('Hi Tom')
else:
    print('Can I talk with tom')
    
input_fname = input('Enter your firstname:').capitalize()
input_lname = input('Enter your last name:').capitalize()

# print(input_lname,', ',input_fname)

print(f'{input_lname}, {input_fname}')
