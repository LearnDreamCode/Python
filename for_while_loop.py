# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 06:10:26 2021

@author: kalai
"""

#for loop is iretation based
# range(<start>,<stop>,<step>)
# start and step are optionnal and the default values are 0 and 1 respectively

# num_list = [0,10,200,3000,40000]
# for num in num_list:
#     num *= num
#     print(num)
    
# for num in range(len(num_list)):
#     print(f'square of index {num} is {num_list[num]*num_list[num]}')
    
    
# #Iteration on range function
# for i in range(0,20,5):
#     n = i*i
#     print (f'square of {i} is {n}')
    
#while loop

# x=1
# while x<10:
#     if x%2:
#         print (f'{x} is an odd number')
#     else:
#         print(f'{x} is a even number');
#     x += 1
# else:
#     print('All elements/numbers were verified')

x=-3
while x<10:
    if x<0: 
        x+=1
        continue
    if x==8: break
    if x%2:
        print (f'{x} is an odd number')
    else:
        print(f'{x} is a even number');
    x += 1
else:
    print('All elements/numbers were verified')
