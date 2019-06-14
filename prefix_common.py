# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:36:07 2019

@author: GRENTOR
"""
def common_prefix():
    list=[]
    for i in zip(*b):
        if (i.count(i[0])==len(i)): 
            list.append(i[0])
        else:
            break
    print(''.join(list))
a=int(input())
b=[]
for i in range(0,a):  
    u=input()
    b.append(u)
common_prefix()

