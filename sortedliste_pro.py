# -*- coding: utf-8 -*-
"""
Created on Thu May 30 07:28:08 2019

@author: GRENTOR
"""

a = int(input())
unsort_list = []
for i in range(a):
    b = list(map(int,input().split()))
    unsort_list.extend(b)
unsort_list.sort()
print(*unsort_list)
#sorted_list = sorted(unsort_list)
#print(" ".join([str(elem) for elem in sorted_list]),end="")