# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 06:04:38 2021

@author: kalai
"""
'''
type - datatype
type(a)
id   - Memory ID
id(a)
dir  - on any object for inspecting
dir(a)
dir(int)
dir(str)
'''

a = 10 

print("type", type(a))

b = 67316843634

print("ID of a",id(a))

print("ID of b",id(b))

print(a.to_bytes(2,byteorder = 'big')) # to contral the memory size (2 bytes)
# b'\x00\n'
print (int.from_bytes(b'\x00\n',byteorder='big'))
# 10

'''
exponential (power(10)) - e
power(2)    - p
'''
c = 20.3423

print(c.hex())

#0x1.457a0f9096bbap+4
print(float.fromhex('0x1.457a0f9096bbap+4'))


# print(a.hex()) # hex only for float

c_num = 10+8j      # complex number
print(c_num.real)

print(c_num.imag)


my_age = 30

print(type(my_age))

my_age = 'my age is 30'

my_age = '29'

print(f'today is my birthday and my age is {int(my_age) + 1}')

greetings = 'Good morning'

print(list(greetings))
#['G', 'o', 'o', 'd', ' ', 'm', 'o', 'r', 'n', 'i', 'n', 'g']
print(tuple(greetings))
#('G', 'o', 'o', 'd', ' ', 'm', 'o', 'r', 'n', 'i', 'n', 'g')
print(set(greetings))
#{'o', 'g', 'd', 'm', 'G', ' ', 'i', 'r', 'n'}
''' 

list: allows duplicate , its in ordered
    
tuple: allows duplicate , its in ordered

Set:  does not allow duplicates and doesn't have the order

'''
my_age = 29
#if my_age == 0:
if my_age:
    print('input age is invalid')
else:
    print(f'the age is {my_age}')


if my_age:
    print(f'the age is {my_age}')
else:
    print('input age is invalid')

    



























