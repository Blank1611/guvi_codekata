# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:19:53 2019

@author: GRENTOR
"""

a = int(input())
b = list(map(int,input().split()))
for i in b:
    if b.count(i) == 1:
        print(i)
    else:
        continue