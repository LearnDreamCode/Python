# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 06:51:37 2021

@author: kalai
"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

fruitdb = myclient["fruitdb"]

fcoll = fruitdb["fcoll"]

updateq = {"name":"Almond"}

updatelist = {"$set":{"selflife":300}}

fcoll.update_one(updateq,updatelist)

updateq = {"name":"Orange"}
updatelist = {"$set":{"selflife":50}}
fcoll.update_one(updateq,updatelist)

updateq = {"name":"lemon"}
updatelist = {"$set":{"selflife":20}}
fcoll.update_one(updateq,updatelist)

updateq = {"name":"dates"}
updatelist = {"$set":{"selflife":365}}
fcoll.update_one(updateq,updatelist)
