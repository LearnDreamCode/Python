# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 06:22:30 2021

@author: kalai
"""

primary_colors={'red','blue','green'}
secondary_colors={'white','aqua','yellow'}

all_colors={}

all_colors=primary_colors.union(secondary_colors)

primary_colors.add('yellow')

all_colors.update({'purple','black'})

all_colors.remove('red')
# print('All Colors: ',all_colors)
# print('Primary Colors',primary_colors)
# print('Intersection',all_colors.intersection(primary_colors))
# print('Symmentric',all_colors.symmetric_difference(primary_colors))
# print('Difference', all_colors.difference(primary_colors))

# print(all_colors.difference_update(primary_colors))

# print(all_colors)

if primary_colors.issubset(all_colors):
    print('priamry colors were included')
else:
    print('No they are not',primary_colors.difference(all_colors) )