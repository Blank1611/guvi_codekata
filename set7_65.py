# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 01:31:56 2019

@author: GRENTOR
"""

n, k = map(int, input().split())
c = list(map(int, input().split()))
b = int(input())
c.pop(k)
if (sum(c)/2) == b:
    print("Bon Appetit")
else:
    print(int(b - (sum(c)/2)))