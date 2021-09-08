# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 05:33:49 2021

@author: kalai
"""

# demo accesssing dict items
# methods: get, items, keys, and values

apple_inv = {
    'name': 'apple',
    'price': 100.00
    }

# access using key
# print(f"We have {apple_inv['inv']} stock of {apple_inv['name']}")

# access using get method
# if the key is not found return a default value
# print(f"We have {apple_inv.get('inv', -1)} stock of {apple_inv.get('name')}")

# items method
print(f"item info:\n{apple_inv.items()}")
print(f"Key info:\n{apple_inv.keys()}")
print(f"Value info:\n{apple_inv.values()}")

for k, v in apple_inv.items():
    print(f"{k}\t\t\t{v}")


# if 'inv' in apple_inv.keys():
#     apple_inv['inv'] += 100000    
#     print(f"We have {apple_inv['inv']} stock of {apple_inv['name']}")
# else:
#     apple_inv['inv'] = 100000    
    

# if 'inv' in apple_inv.keys():
#     apple_inv['inv'] += 100000    
#     print(f"We have {apple_inv['inv']} stock of {apple_inv['name']}")
# else:
#     apple_inv['inv'] = 100000    

for v in apple_inv.values():
    print(v)