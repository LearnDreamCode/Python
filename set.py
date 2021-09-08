# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 06:09:38 2021

@author: kalai
"""
# muttable
# un-ordered
# Can't index or slice it
# Item are hashable
# Can't have dups in the set
s_fruit_name ={'Apple','Orange','Mango','Grapes','Cherry'}

s_fruit_name.add('Jackfruit')

# print(s_fruit_name.pop())

s_fruit_name.remove('Grapes')

for i in range(len(s_fruit_name)):
    print(s_fruit_name.pop())
print(s_fruit_name)   
s_fruit_name.update({'fig'})

print(s_fruit_name)