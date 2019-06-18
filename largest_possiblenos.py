# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:06:45 2019

@author: GRENTOR
"""
b = int(input())
a = list(map(int,input().split()))
if len(a) == a.count(0):
    print(0)
else:
    a.sort(reverse=True)
    print(''.join(str(elem)for elem in a))
