# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 23:58:33 2019

@author: GRENTOR
"""

a, b = map(str, input().split())
if abs(len(set(a)) - len(set(b))) == 1 and len(a) == len(b):
    print("yes")
else:
    print("no")
    
for i,j in zip(a,b):
    print(i,j)
    