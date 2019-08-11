# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 22:22:06 2019

@author: GRENTOR
"""

n = int(input())
a = list(map(int, input().split()))
max_sum = 0
for i in range(len(a)):
    st = a[i::]
    for j in range(2,len(a[i::])):
        if max_sum<sum(a[i::j]):
            max_sum = sum(a[i::j])
print(max_sum)