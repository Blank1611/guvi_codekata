# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:11:50 2019

@author: GRENTOR
"""

a = (input().lower())
vowel='aeiou'
if a.isalpha():
    if a in vowel:
        print("Vowel",end = "")
    else:
        print("Consonant",end = "")
else:
    print("invalid")
