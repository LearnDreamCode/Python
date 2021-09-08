# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 05:48:06 2021

@author: kalai
"""

primary_colors = {'red', 'blue', 'green'}
secondary_colors = {'aqua', 'purple', 'orange'}

all_colors = set()

all_colors = primary_colors.union(secondary_colors)

primary_colors.add('yellow')
all_colors.update({'white', 'black'})

print(all_colors.difference(primary_colors))
print(all_colors.intersection(primary_colors))
print(all_colors.symmetric_difference(primary_colors))

# difference update
print(all_colors.difference_update(primary_colors))
