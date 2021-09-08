# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 20:24:11 2021

@author: kalai
"""

i_string=input('Enter a string : ')
ln_alpha=0
ln_numeric=0
ln_special=0
for i_char in i_string:
    if i_char.isalpha():
        ln_alpha+=1
    elif i_char.isnumeric():
        ln_numeric+=1
    else:
        ln_special+=14
print('Alphabets =',ln_alpha)
print('Numeric =',ln_numeric)
print('Others =',ln_special)
print('Total =',len(i_string))
