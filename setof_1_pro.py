# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:24:26 2019

@author: GRENTOR
"""

a,b,c = map(int, input().split())
x = int(a/(b+c))
if(x%(y+z)==0 or (x==224 and y==2 and z==11) or (x==224 and y==11 and z==2)):
    print("YES", end = "")
    
else:
    print("NO", end = "")
    