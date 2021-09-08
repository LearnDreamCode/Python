# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 06:46:32 2021

@author: kalai
"""

fo=open('Student_info.txt','r')

f_student_mark_info= fo.readline()
Nl_studMark_info=[]
while f_student_mark_info!='':
    l_studMark_info=f_student_mark_info.strip('\n').split(',')
    l_studMark_info= [x.lstrip(' ') for x in l_studMark_info]    
    Nl_studMark_info.append(l_studMark_info)
    f_student_mark_info=fo.readline()
print(Nl_studMark_info)
    
print('End of file')