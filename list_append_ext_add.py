# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 06:12:26 2021

@author: kalai
"""

import random

l_number = [random.randint(10, 100) for _ in range(1,10)]

l_number.append(200)

print ('Append 200 :'+l_number)

l_number.extend([300,400])

print ('Extend with 300,400 : ',l_number)

l_number.insert(5, 500)

print('insert 500 at 5th index pos : ',l_number)

l_number.remove(200)

print('Remove 200 from list: ', l_number)

#disply and remove the last element
l_number.pop()

#display and remove the element in 10th index pos
l_number.pop(10)
# asc (default)
print('Asc order : ',l_number.sort())
#desc
print('Desc order : ',l_number.sort(reverse=True))

print('Reverse the elements by index position: ',l_number.reverse())
# reverse using Index
print(l_number[::-1])
