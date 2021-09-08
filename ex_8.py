# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 09:27:46 2021

@author: kalai
"""
#Q1
i_string=input('Enter a String: ')
position=0
o_string=''
for i in range(len(i_string)):
    if not(i%2):
        o_string+=i_string[i]
print(o_string)
#Q2
print(input('Enter a string: ')[-4:]*3)
#q3
i_string=input('Enter a string')
o_string= i_string[0:5] if len(i_string)>4 else i_string
print(o_string)
#q4
n=4
ref='abcdefghijklmnopqrstuvwxyz'
ref+=ref[0:n]
i_string='balax'
o_string=''
for i in i_string:
    o_string+=ref[ref.index(i)+n]
print(o_string)

