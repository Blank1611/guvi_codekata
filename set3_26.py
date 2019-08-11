# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 00:57:36 2019

@author: GRENTOR
"""

n = int(input())
a = list(map(int, input().split()))
tse = []
for i in range(len(a)):
    st = a[i::]
    ts = []
    ts.append(st[0])
    for j in range(1, len(st)):
        if (st[j]==st[-1]):
            ts.append(st[j])
        elif (st[j]>=st[j-1]):
            ts.append(st[j])
        else:
            
            break
    tse.append(ts)

print(len(max(tse, key = len)))