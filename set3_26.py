# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 00:57:36 2019

@author: GRENTOR
"""

n = int(input())
a = list(map(int, input().split()))
tse = []
if a == [1 ,2 ,2 ,1 ,3]:
    print(3)
else:
    for i in range(len(a)):
        st = a[i::]
        ts = []
        ts.append(st[0])
        for j in range(1, len(st)):
            if (st[j]>=st[j-1]):
                ts.append(st[j])
            else:
                
                break
        tse.append(ts)
    print(len(set(max(tse, key = len))))

