# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 06:35:32 2021

@author: kalai
"""

# Q1: Given a text, “Mary had a little lamb. His fleece was black as coal, yeah. 
#     Everywhere the child went. That little lamb was sure to go now”.
# - convert this into a list
# - find the longest word

input_string = 'Mary had a little lamb. His fleece was black as coal, yeah. Everywhere the child went. That little lamb was sure to go now'
l_string = input_string.split()
prev_word_len = 0
for i_word in l_string:
    if len(i_word) > prev_word_len:
        long_word = i_word
        prev_word_len = len(i_word)
print(f'the longest word in the inupt strng is "{long_word}"')