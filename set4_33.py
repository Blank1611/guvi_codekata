# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:56:10 2019

@author: GRENTOR
"""

a = input()
print(a[a.index(max(a[1::], key = lambda x: a[0]<x))::])