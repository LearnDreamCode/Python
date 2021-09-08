# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 06:31:20 2021

@author: kalai
"""

import math

while True:
    try:
        r = float(input ('Enter the radius value: ') )
        
        if r <= 0:break
        
        area_circle = math.pi * r ** 2
        
        print(f'The area of circle with radius {r} is {area_circle}')
        
    except ValueError:
        print('Only numbers allowed for radius value')
        
print ("Thank you")

def fn_calc():
    '''
    This function is to perform mathematical operations on 2 numbers and return the output result.

    Returns
    -------
    number.

    '''    

    while True:
        ln_operation = input ('''a -- Add
                              s  : subtract
                              m  : multiply
                              d  : division
                              fd : floor division
                              md : Modulus
                              q  : quit
                              Enter the prefered operation''').lower()
                              
        if ln_operation == 'q':break
        
        a = float(input('enter the 1st number :'))
        
        b = float(input('enter the 2nd number :'))
        
        if   ln_operation == 'a':
            c = a+b
        elif ln_operation == 's':
            c = a-b
        elif ln_operation == 'm':
            c = a*b
        elif ln_operation == 'd':
            c = a/b
        elif ln_operation == 'fd':
            c = a//b
        elif ln_operation == 'md':
            c = a%b
        return c

fn_calc()
    