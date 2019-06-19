# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:11:56 2019

@author: GRENTOR
"""
num = int(input())
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print('no')
           break
   else:
       print('yes')
else:
   print('no')