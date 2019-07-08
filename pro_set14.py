# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 00:11:15 2019

@author: GRENTOR
"""

def xor(l):
    el = 0
    for i in l:
        el^=i
    return el
n,q = map(int, input().split())
liste = list(map(int, input().split()))
for i in range(q):
    a,b = map(int, input().split())
    sa = xor(liste[a-1:b])
    print(sa)
    
#[el^=elem for elem in l[a-1:b]]