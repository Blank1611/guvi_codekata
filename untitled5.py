# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:42:18 2019

@author: GRENTOR
"""

a = int(input())
b = list(map(int, input().split()))
c=[]
for i in range(a):
    if(i == b[i]):
        c.append(b[i])
c.sort()
if len(c) == 0:
    print(-1)
else:
    print(*c)