# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 06:39:50 2021

@author: kalai
"""

apple_inv = {
    'name': 'apple',
    # 'inv': 100000,
    'price':100.00
    }

#update takes one k,v pair at a time
apple_inv.update({'name': 'Kashmir_apple'})

apple_inv.update({'inv':50000})
#pop
print(apple_inv.pop('price'))

print(apple_inv)

#popitem remove the last K,V pair

print(apple_inv.popitem())

print(apple_inv)