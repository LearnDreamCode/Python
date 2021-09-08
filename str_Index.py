# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 23:10:37 2021

@author: kalai
"""

#find
greetings='Good morning'
# <str>.index(<serach str>,[start],[end])

# 'o' occuring for the first time
print('starting position is: ', greetings.index('o'))

# 'o' occuring after the 2nd index position
print('starting position is: ', greetings.index('o',2))


# 'o' occuring after the 3nd index position but before 6th position
# print('starting position is: ', greetings.index('o',3,6))
# No result

# 'o' occuring after the 3nd index position but before 7th position
print('starting position is: ', greetings.index('o',3,7))