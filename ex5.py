# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:32:21 2021

@author: kalai
"""
## Q1
# i_string=list(input('enter the string : '))
# i_index_pos=int(input('Enter the index to be removed : '))

# # i_string.remove(i_index_pos)
# i_string.pop(i_index_pos)
# print(''.join(i_string))

## Q2
# i_string=input('Enter a deimal vale : ')
# ref_index=i_string.index('.')
# print(i_string[:ref_index+3])

##Q3
i_string=input('Enter a string : ').casefold()
i_subString=input('Enter the sub-string : ').casefold()
print(i_string, '-',i_subString)
if i_string.find(i_subString) >= 0:
    print(i_string.count(i_subString))
else:
    print('not found')