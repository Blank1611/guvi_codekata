# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 21:34:43 2019

@author: GRENTOR
"""

N,Q = map(int, input().split())
liste = list(map(int, input().split()))
for i in range(Q):
    a,b = map(int, input().split())
    sa = lambda a,b: sum(liste[a-1:b])
    print(sa(a,b))