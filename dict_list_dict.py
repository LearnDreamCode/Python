# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 06:45:17 2021

@author: kalai
"""

apple_inv = {
    'name': 'Jackfruit',
    'inv': 10000,
    'price':100.00
    }

# apple_inv_l = [set(k,v) for k,v in apple_inv]  // check this

apple_inv_l =[('name', 'Jackfruit'),
    ('inv', 10000),
    ('price',100.00)]
apple_inv_dict = {k:v for k,v in apple_inv_l}

