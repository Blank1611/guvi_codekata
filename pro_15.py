# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 00:31:23 2019

@author: GRENTOR
"""
def bina(elem):
    return bin(elem)

it = int(input())
a = list(map(int, input().split()))
s = sorted(a, key = bina, reverse = True)
for i in s:
    print(i)

