# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:58:22 2019

@author: GRENTOR
"""
def posi_nega(n):
    if n==0:
        print("Zero", end = "")
    elif n>0:
        print("Positive",end = "")
    elif n<0:
        print("Negative",end = "")
a = int(input())
posi_nega(a)
