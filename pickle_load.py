# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 06:42:15 2021

@author: kalai
"""

import pickle

f_obj=open('stud_mark_dtl.pckl','rb')

stud_info_out=pickle.load(f_obj)
print(stud_info_out)