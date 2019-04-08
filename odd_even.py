# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:47:51 2019

@author: GRENTOR
"""
def odd_even(n):
    if n<0:
        print("invalid")
    else:
        if n%2==0:
            print("Even")
        elif (n%2)>0:
            print("Odd")
a = input()
if a.isdigit():
    a=int(a)
    odd_even(a)
else:
    print("invalid")
