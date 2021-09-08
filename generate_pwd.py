# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 06:22:48 2021

@author: kalai
"""

# Q: Generate a password of 8 characters long
# - one of them should be upper case
# - one of them should be numeric
# - one of them should be a special character

import random
# numList = [random.randint(0, 10)]
# print('int',numList)
# numList = [random.randrange(0, 10, 3)]
# print('range',numList)

low_case = ''.join([chr(int(random.randint(97,122))) for i in range(0,3)])
num = chr(random.randint(48,57))
up_case = chr(random.randint(65,90))
special_char = chr(random.randint(33,47))
low_case2 = ''.join([chr(int(random.randint(97,122))) for i in range(2)])

temporary_pwd = low_case+num+up_case+special_char+low_case2

print(f'Your temporary password is {temporary_pwd}')

import random
# numList = [random.randint(0, 10)]
# print('int',numList)
# numList = [random.randrange(0, 10, 3)]
# print('range',numList)

#lower case
pwd = [chr(random.randint(97,122)) for i in range(3)]
#number
pwd.append(chr(random.randint(48,57))) 
#uppper case
pwd.append(chr(random.randint(65,90)))
#Special Character
pwd.append(chr(random.randint(33,47)))
temporary_pwd = ''.join(pwd+[chr(random.randint(97,122)) for i in range(2)])

print(f'Your temporary password is {temporary_pwd}')


import random
#lower case
pwd = ''.join([chr(random.randint(97,122)) for i in range(3)])
#number
pwd+=(chr(random.randint(48,57))) 
#uppper case
pwd+=(chr(random.randint(65,90)))
#Special Character
pwd+=(chr(random.randint(33,47)))
temporary_pwd = pwd+''.join([chr(random.randint(97,122)) for i in range(2)])
print(temporary_pwd)


import random
#lower case
pwd=''
for i in range(5):     # not sure whether I could replace this with map 
    pwd+= chr(random.randint(97,122))
#number
pwd+=(chr(random.randint(48,57))) 
#uppper case
pwd+=(chr(random.randint(65,90)))
#Special Character
pwd+=(chr(random.randint(33,47)))
print(pwd)


import random
#lower case
pwd=''
for i in range(8):
    if i==2:
       #number
       pwd+=(chr(random.randint(48,57)))
       continue
    if i==4:
       #uppper case
       pwd+=(chr(random.randint(65,90)))
       continue
    if i==6:
       #Special Character
       pwd+=(chr(random.randint(33,47)))
       continue
    pwd+= chr(random.randint(97,122))
print(pwd)