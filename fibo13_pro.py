# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 00:00:11 2019

@author: GRENTOR
"""


a = int(input())
b = list(map(int, input().split()))
summ = 0
for i in range(1,len(b)):
    for x in b[:i]:
        if x<b[i]:
            summ+=x
print(summ, end = "")
