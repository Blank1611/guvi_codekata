# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:20:41 2019

@author: GRENTOR
"""

a = int(input())
if a%2==0:
    print(int((a//2)*(a-1)))
else:
    print(int(a*(a//2)))