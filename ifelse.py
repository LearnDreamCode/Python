# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 23:26:39 2021

@author: kalai
"""
def fn_cal():
    '''
    

    Returns
    -------
    Number.

    '''
        
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
    else:
        return 'Invalid operation'  
    
    return c
               
           
while True:
    ln_operation = input ('''
                          a  : Add
                          s  : subtract 
                          m  : multiply 
                          d  : divide 
                          fd : floor divide 
                          md : Modulus
                          q  : quit \nEnter the prefered operation : ''').lower()
    
    if ln_operation == 'q':
        print( 'Thank you')
        break   
    
    a = float(input('enter the 1st number :'))
    
    b = float(input('enter the 2nd number :'))
    
                          
    res = fn_cal()
    print ( res  )

    
    
    
    
    
    
    