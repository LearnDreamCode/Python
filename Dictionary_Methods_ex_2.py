# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 06:12:15 2021

@author: kalai
"""

apple_inv = {
    'name': 'apple',
    # 'inv': 100000,
    'price':100.00
    }

# print(f"we have {apple_inv['inv']} stock of {apple_inv['name']}")

# #dictionary.get('<key>',<default value if the key is not found>)1

# print(f"We have {apple_inv.get('inv',-1)}" )

for k,v in apple_inv.items():
    print(f"{k} \t\t\t {v}")
    
if 'inv' in apple_inv.keys():
    print(f"We have {apple_inv['inv']} {apple_inv['name']}")
else:
    print("check and update the stock for apple")
    apple_inv['inv']=int(input('Enter the apple in stock'))

for v in apple_inv.values():
    print(v)
    
print(f"fruit info: \n{apple_inv.items()}")