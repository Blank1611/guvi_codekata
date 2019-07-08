# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:39:07 2019

@author: GRENTOR
"""

n,q = map(int, input().split())
liste = list(map(int, input().split()))
for i in range(q):
    a,b = map(int, input().split())
    sa = lambda a,b: min(liste[a-1:b])
    print(sa(a,b))