# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:43:13 2019

@author: GRENTOR
"""

num = int(input())
list_pow = list(map(lambda m: m*num, range(1,6)))
print(*list_pow)
