# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 00:00:11 2019

@author: GRENTOR
"""
def fibo(z):
    s=0
    for i in range(0,z):
        s+=i
    return s
a = int(input())
b = list(map(int, input().split()))
result = list(map(fibo, b))
print(sum(result))
