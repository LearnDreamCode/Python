# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 06:42:06 2021

@author: kalai
"""

import sys

current_version = int(sys.version[0])

if current_version != 3:
    sys.exit()
else:
    print('The current version is 3. We are good to proceed')