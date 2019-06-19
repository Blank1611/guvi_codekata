# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:20:41 2019

@author: GRENTOR
"""
a, b = map(int, input().split())
def armstrong_check(num):
    num = str(num)
    amrno = 0
    for i in range(len(num)):
        amrno += int(num[i])**len(num)
        
    if int(num) == amrno:
        return True
    else:
        return False



result = prime_list = list(filter(armstrong_check,range(a, b)))
print(*result)