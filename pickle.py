# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 07:20:16 2021

@author: kalai
"""

import pickle

stud_info=[['Sundar,82,100'],['Kalai,89,92'],['swathi,100,90'],['varun,100,98']]
#wb - write binary
f_obj=open('stud_mark_dtl.pckl','wb')
pickle.dump(stud_info,f_obj)

