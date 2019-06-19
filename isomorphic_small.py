# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 23:21:19 2019

@author: GRENTOR
"""
a, b = map(str, input().split())
def isIsomorphic(w1,w2) : 
    if len(w1) != len(w2): return False
    return [len(set(w1)),len(set(w2))] == 2 * [len(set(zip(w1,w2)))]
if isIsomorphic(a,b):
    print("yes")
else:
    print("no")