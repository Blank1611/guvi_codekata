# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 16:59:22 2019

@author: GRENTOR
"""

a = int(input())
b = list(map(int,input().split()))
rep = []
for i in range(len(b)):
    if b.count(b[i]) > 1:
        if b[i] not in rep:
            rep.append(b[i])
rep.sort()
if len(rep)==0:
    print("unique")
else:
    print(" ".join([str(elem) for elem in rep]),end="")
        