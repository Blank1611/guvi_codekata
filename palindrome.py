# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:16:35 2019

@author: GRENTOR
"""

def rev(a): 
    return a[::-1] 
  
def isPalindrome(a): 
    revstr = rev(a)  
    if (a == revstr): 
        return True
    return False

a = input()
ans = isPalindrome(a) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 