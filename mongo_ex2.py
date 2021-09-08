# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 06:38:26 2021

@author: kalai
"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

fruitdb = myclient["fruitdb"]

fcoll = fruitdb["fcoll"]

colorq = {"fruitcolor":"brown"}

fruits=fcoll.find(colorq,{"_id":0,"name":1,"fruitcolor":1})
    
for f in fruits:
    print(f)