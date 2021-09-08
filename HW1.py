# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 08:05:35 2021

@author: kalai
"""

ls_print = '{}'.format(input('Enter the sting to be displayed :'))


print(ls_print)

'''
StringVar = 'Hello Tutorialspoint'
print("\"%s\""% StringVar )
print("\\%s\\"% StringVar )
print('"%s"' % StringVar )
print('"{}"'.format(StringVar))
'''

'''Q: get a number from the user, check whether the number is even or not... 
if even print the square of the number else print the actual number'''

try:
    x = int(input('Enter an Integer '))
    y = x % 2
    if y:
        print(x)
    else:
        print(pow(x,2))
except ValueError:
    print ('The input is not a valid interger')
    
    