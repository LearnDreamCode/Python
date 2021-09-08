# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:37:10 2021

@author: kalai
"""

i_length = int(input('Enter the lentgh of rectangle: '))
i_width = int(input('Enter the width of rectangle: '))

for i in range(i_length):
    if i==0 or i == i_length-1:
        print('*'*i_width)
    else:
        print('*'+' '*(i_width-2)+'*')
