# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:38:32 2019

@author: GRENTOR
"""

a = input().upper()
if a[len(a)-1] == "X" or a[len(a)-1] == "V":
    print( 5*a.count('V') + 10*a.count('X') - 1*a.count('I'))
else:
    print(1*a.count('I') + 5*a.count('V') + 10*a.count('X'))