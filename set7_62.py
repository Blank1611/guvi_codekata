# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:30:39 2019

@author: GRENTOR
"""

def palindrome(ls):
    pal_ls = []
            
    for i in range(len(ls)-1):
        if len(max(pal_ls, default = ''))<len(ls[i:]):
            for j in range(2,len(ls[i:])+1):
                #t1 = temp[0:j]
                #print(t1)
                t1 = ls[i:i+j]
                if t1 == t1[::-1]:
                    if(t1 not in pal_ls) and (len(t1)>len(max(pal_ls, default = ''))):
                        pal_ls.append(t1)
    return (len(ls) - len(max(pal_ls, default = '')))
inp = input().lower()
print(palindrome(inp))