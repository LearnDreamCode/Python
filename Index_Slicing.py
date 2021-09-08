# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 06:03:35 2021

@author: kalai
"""

# Strings



greetings='Good Morning'

#indexing one character at a time.
# represented in []


# #Print the first character - G
# print(greetings[0])

# #Print the 5th index / sixth character - M
# print(greetings[5])

# #Print the first character from last - g
# print(greetings[-1])

# #Print the fourth character from last - n
# print(greetings[-4])

# for c in greetings:
#     print(c)

#slicing [start:stop:step]
#default [0:len(str):1]
# print(greetings[0:5])
# print(greetings[:5])

#display Morn
# print(greetings[5:9])

# #display Morn with negative slicing
# print(greetings[-7:-3])

# #print the given string in reverse
# print(greetings[::-1])
#[start from -1: -(len(str)):each character from reverese(-1)]

# Variables and expressions are allowed but it should result in int type

# print the middle character of thr given string
# print(greetings[len(greetings)//2])


if len(greetings)%2:
    print(greetings[len(greetings)//2])
else:
    print(greetings[len(greetings)//2:(len(greetings)//2)+2])

