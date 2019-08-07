# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 01:27:42 2019

@author: GRENTOR
"""

import math
a = int(input())
f = lambda x: x - 2**(int(math.log2(x))) if 2**(int(math.log2(x))) != 2**(math.log2(x)) else 0
print(f(a))