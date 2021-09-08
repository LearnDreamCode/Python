# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:03:24 2021

@author: kalai
"""

# Q3: Write a Python program to get a string made of the first 2 and the
# last 2 chars from a given a string. If the string length is less than 2,
# return an empty string, for example, if:
#  sample_string = "abcdefghij", the expected_output = "abij"
#  sample_string = "ab", the expected_output = "abab"
#  sample_string = "a", the expected_output = ""

i_string = input('Enter a string: ')
if len(i_string)>=2:
    print(i_string[:2]+i_string[-2:])
else:
    print('')