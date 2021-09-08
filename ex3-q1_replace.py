# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:09:27 2021

@author: kalai
"""

# Q1: Change all occurrence of the first character of a string to ‘$’ except for the first character.
# for example, input_string = ‘abracadabra’ expected_output = ‘abr$c$d$br$’

input_string = 'abracadabra'
f_char = input_string[0]
input_string=input_string.replace(f_char, '$')
print(f_char+input_string[1:])
