# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 06:14:26 2021

@author: kalai
"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

fruitdb = myclient["fruitdb"]

fcoll = fruitdb["fcoll"]
# fruitdoc1= {"name":"dates","fruittype":"desert","location":"Rajasthan",
#              "fruitsize":"small","fruitcolor":"brown","shelflife":"365",
#              "deletecode":0,"remarks":"Added"
#              }

# fcoll.insert_one(fruitdoc1)

fruitdoc2= [{"name":"Almond","fruittype":"desert","location":"Rajasthan",
            "fruitsize":"small","fruitcolor":"brown","shelflife":"365",
            "deletecode":0,"remarks":"Added"
            },
            {"name":"Orange","fruittype":"Citric","location":"Australia",
            "fruitsize":"Medium","fruitcolor":"Orange","shelflife":"365",
            "deletecode":0,"remarks":"Added"
            },
            {"name":"Lemon","fruittype":"Citric","location":"Chennai",
            "fruitsize":"small","fruitcolor":"yellow","shelflife":"365",
            "deletecode":0,"remarks":"Added"
            },
            ]

fcoll.insert_many(fruitdoc2)





