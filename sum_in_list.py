# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:56:33 2019

@author: GRENTOR
"""

a,b = map(int,input().split())
c = list(map(int,input().split()))
for i in range(b+1):
    sum=0
    sum += c[i]
print(sum)