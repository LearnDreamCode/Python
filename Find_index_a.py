# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 06:16:27 2021

@author: kalai
"""

magic_word =  'abracadabra'
search_str = 'a'
start_pos=0
iteration_count=len(magic_word)-len(magic_word.replace('a', '') ) 
for i in range(iteration_count):
    start_pos=magic_word.index(search_str,start_pos)
    print('a is present at the position ',start_pos)
    start_pos+=1
print('sreach completed')