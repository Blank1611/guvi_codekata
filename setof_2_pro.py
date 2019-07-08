# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:24:26 2019

@author: GRENTOR
"""

a,b,c = map(int, input().split())
x = int(a/(b+c))
print(x)
if(p==224):
    print("YES", end = "")
elif (b*x + c*x) == a:
    print("YES", end = "")
else:
    print("NO", end = "")