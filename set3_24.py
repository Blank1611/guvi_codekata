# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 03:09:12 2019

@author: GRENTOR
"""

a = int(input())
def binar(s):
    arr = list(map(lambda fr: format(fr, 'b'), range(0, (2**a))))
    arr = sorted(arr, key = lambda x: x.count('1'))
    arr = list(map(lambda x: '0'*(a-len(x))+x, arr))
    return arr
for i in binar(a):
    print(i)