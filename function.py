# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 06:07:00 2021

@author: kalai
"""
import random
# Function: def <function_name> [argument1,argument2,..]
# return an object to the calling module

def generate_rand_num():
    '''
    This function is used to return random integers

    Returns
    -------
    None.

    '''
    return random.randint(10,100)


print(generate_rand_num())

# if the arguments are missing, it will return the function objects
print(generate_rand_num)

#function with arguments
def generate_rand_int(start,end):
    '''
    This function is used to return random integers

    Returns
    -------
    None.

    '''
    return random.randint(start,end)


print(generate_rand_int(50,500))

#function with default values
def generate_rand_int_def(end,start=10):
    '''
    This function is used to return random integers

    Returns
    -------
    None.

    '''
    return random.randint(start,end)

print(generate_rand_int_def(end = 110))
