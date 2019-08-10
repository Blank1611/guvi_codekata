# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 02:02:04 2019

@author: GRENTOR
"""

a = int(input())
b = list(map(int, input().split()))
def aveg(c, d):
    lsum = 0
    #flag = False
    for i in range(len(d)-1):
        lsum += d[i]
        rsum = sum(d) - lsum
        if (lsum*(c-i-1)) == (rsum*(i+1)):
            return 'yes'
        
    return 'no'
print(aveg(a,b))
    