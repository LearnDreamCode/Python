# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:47:27 2021

@author: kalai
"""

# Q2: For the following string: 'The quick brown fox jumped over the lazy dog'
#  a. extract the first 5 characters of the string
#  b. extract the last 5 characters of the string (use -ve indexing)
#  c. extract the middle 5 characters of the string (use len)

i_string='The quick brown fox jumped over the lazy dog'

print('First 5 characters are :'+i_string[0:5])
print('Last 5 characters are :'+i_string[-5:])
if len(i_string)%2:
    print('Middle 5 characters are :'+i_string[(len(i_string)/2)-3:(len(i_string)/2)+3])
else:
    print('Middle 5 characters are :'+i_string[(len(i_string)//2)-3:(len(i_string)//2)+3])
