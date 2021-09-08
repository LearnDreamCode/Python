# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 05:48:22 2021

@author: kalai
"""

# demo union
primary_colors = {'red', 'blue', 'green'}
secondary_colors = {'aqua', 'purple', 'orange'}

all_colors = set()

all_colors = primary_colors.union(secondary_colors)

primary_colors.add('yellow')
all_colors.update({'white', 'black'})


if primary_colors.issubset(all_colors):
    print('Yes it is')
else:
    print('No they are not', primary_colors.difference(all_colors))