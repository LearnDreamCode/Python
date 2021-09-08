# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 20:10:48 2021

@author: kalai
"""

i_string='hoW are you'

print(i_string.title())


for i in i_string:
    if i_string.count(i) >1:
        i_string=i_string.replace(i,'')
print(i_string)

i_num_string=input('Enter the numbers')
if i_num_string.isnumeric():
    print(sum([int(x) for x in i_num_string]))


i_string = '01100100010011000001'
l_count=o_count=0
for i in i_string:
    if i=='0':
        l_count+=1
    else:
        l_count=0
    if o_count<l_count:
       o_count=l_count
print(o_count)
        
i_string='bala sundar'.title().split()
o_string=''
print(i_string)
o_string=' '.join([word[:-1]+word[-1].upper() for word in i_string])
print(o_string)

        