# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:38:55 2021

@author: kalai
"""

# i_string='aabbbcde'
# l_occurance=[]
# for x in set(i_string):
#     l_occurance.append([i_string.count(x),x])
# l_occurance.sort(reverse=True)
# print(l_occurance)


i_string='aabbbcde'
lst=list(set(i_string))
lst.sort()
l_occurance=[]
for x in lst:
    l_occurance.append([i_string.count(x),x])
l_occurance.sort(reverse=True)
print(l_occurance[:3])

# have to sort by 2nd element.
