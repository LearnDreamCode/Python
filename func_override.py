# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 06:30:35 2021

@author: kalai
"""
import random

#override the default value
def gen_rand_int_oride(start=100,end =1000):
    return random.randint(start, end)

print(gen_rand_int_oride())
print('override end =102 : ',gen_rand_int_oride(end =102))
print('override both start and end : ',gen_rand_int_oride(102,105))
