# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 06:46:31 2021

@author: kalai
"""

#split
greetings = ' Good morning, How are you?'

# split default delimiter is ' ' and return the result as list object
# print(greetings.split())
# print(greetings.split(','))


# print(greetings.split('are'))


# is

print(greetings.isalpha())
print(greetings.isalnum() )

greetings = 'GoodMorning'

print(greetings.isalpha())
print(greetings.isalnum())
print(greetings.isnumeric())