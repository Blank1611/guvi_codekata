# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:19:08 2019

@author: GRENTOR
"""

N = input().lower()
Q = input().lower()
a = '0abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
for i in range(len(N)):
    print(a[a.index(Q[i])+a.index(N[i])], end = '')