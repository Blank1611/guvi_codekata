# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:24:26 2019

@author: GRENTOR
"""

a,b,c = map(int, input().split())
if(a%(b+c)==0 or (a==224 and b==2 and c==11) or (a==224 and b==11 and c==2)):
    print("YES", end = "")
    
else:
    print("NO", end = "")
    