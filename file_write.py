# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 07:45:25 2021

@author: kalai
"""

# fetch the latitude and longitude for a city in India

# import pyodbc
import datetime as dt
# today = dt.date.now()
f_name =  'latitude'+dt.datetime.now().strftime("%Y%m%d%H%M%S%f")+'.txt'
print(f_name)

fo = open(f_name, 'w')

row =  [1,2,3,4]
for i ,rec in enumerate(row):
    fo.write(str(rec) + '\n')
    print(str(rec))
    total_record = 'Total_record count is '+str(i)
fo.write(total_record)
print(f'Total_record count is {total_record}')
fo.close()
