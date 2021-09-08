# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 06:32:19 2021

@author: kalai
"""
import random
def gen_rand_num_list(start=10,end=100,n=5):
    '''
    

    Parameters
    ----------
    start : TYPE, optional
        DESCRIPTION. The default is 10.
    end : TYPE, optional
        DESCRIPTION. The default is 100.
    n : TYPE
        DESCRIPTION. number of elements

    Returns
    -------
    return list of random numbers.

    '''
    return [random.randint(start,end) for _ in range(n)]

def gen_pwd (start=ord('A'),end=ord('z'),n=8):
    '''
    

    Parameters
    ----------
    start : TYPE, optional
        DESCRIPTION. The default is ord('A').
    end : TYPE, optional
        DESCRIPTION. The default is ord('z').
    n : TYPE
        DESCRIPTION. No.of, characters

    Returns
    -------
    None.

    '''
    return [chr(random.randint(start,end)) for _ in range(n)]

print(''.join(gen_pwd()))