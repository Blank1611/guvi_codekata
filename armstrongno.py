# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:43:29 2019

@author: GRENTOR
"""

num = input()


def armstrong_check(num):
    amrno = 0
    for i in range(len(num)):
        amrno += int(num[i])**len(num)
        
    if int(num) == amrno:
        print("yes")
    else:
        print("no")
armstrong_check(num)