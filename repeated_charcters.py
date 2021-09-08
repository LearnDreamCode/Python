# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 06:44:20 2021

@author: kalai
"""

# Q3:
# o4 e3 u2 h2 r2 t2
# print the repeated characters in a string.
#  Sample string: 'the quick brown fox jumps over the lazy dog'
#  Expected output : o4 e3 u2 h2 r2 t2
 
input_string= 'the quick brown fox jumps over the lazy dog'
s_string = set(input_string)
#print(s_string)
opt_string=''
opt_string_sort=''

for i in s_string:
    char_count = input_string.count(i)
    if i != ' ' and char_count>1:  #len(input_string)-len(input_string.replace(i, '')) > 1:
        opt_string+=str(char_count)+i+' '
        
list_opt_string=opt_string.split()
list_opt_string.sort(reverse=True)
# print(list_opt_string)

for i in list_opt_string:
	opt_string_sort+=' '+i[::-1]
    
print(opt_string_sort.lstrip())


