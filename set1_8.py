# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 03:05:36 2019

@author: GRENTOR
"""

import math
import functools
N, Q = map(int, input().split())
lis = list(map(int, input().split()))
for i in range(Q):
    L, R = map(int, input().split())
    print(functools.reduce(math.gcd, lis[L-1 : R]))