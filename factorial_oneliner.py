# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:34:51 2019

@author: GRENTOR
"""

fact = lambda n:1 if n==0 else n*fact(n-1)
print(fact(0))