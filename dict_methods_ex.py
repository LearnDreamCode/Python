# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 05:47:43 2021

@author: kalai
"""

# sets are unordered
# you can't index it or slice it
# items are hashable
# you can't have dups in the set
fn = {'apple', 'banana', 'mango', 'figs', 'grapes', 'cherry', 
      'berry', 'apple', 'apple'}

print(fn)
fn.add('strawberry')
print(fn.pop())
print(fn)
print(fn.remove('strawberry'))
print(fn)
# for i in range(len(fn)):
#     print(fn.pop())

fn.update({'rasberry'})