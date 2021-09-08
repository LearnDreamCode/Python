# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 06:35:38 2021

@author: kalai
"""
fo=open('Student_info.txt','r')
f_student_info = fo.readline()

while f_student_info != '':
    print(f_student_info, end ='')
    f_student_info = fo.readline()
print('End of file')
