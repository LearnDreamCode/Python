# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 06:05:45 2021

@author: kalai
"""

# whitespace - space , \n, \t
# strip - remove leading and trainling whitespace
#lstrip
#rstrip
# input_string = input('Enter you message:')
# print('As is : ', '$' + input_string + '$')
# print('strip is : ', '$' + input_string.strip() + '$')
# print('lstrip is : ', '$' + input_string.lstrip() + '$')
# print('rstrip is : ', '$' + input_string.rstrip() + '$')


input_fname = input('Enter your firstname:').strip().capitalize()
input_lname = input('Enter your last name:').strip().capitalize()

print(input_lname+', '+input_fname)

# print(f'{input_lname}, {input_fname}')