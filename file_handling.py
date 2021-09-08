# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 06:17:11 2021

@author: kalai
"""

# flat file / sequential file handling
# read and write flat files

#open function
#No.of.paramenters: 2
#1: file_name
#2: mode in which we need to open the file

# open is successful then it will return  file object (file handler)

fo=open('Student_info.txt','w')

fo.write('Alvin, 87, 98\n')
fo.write('Amar, 100, 100\n')
fo.write('Arun, 75, 93\n')
fo.write('Babu, 87, 96\n')
fo.write('Cathy, 89, 98\n')
fo.write('Kaai, 100, 98\n')

fo.close()