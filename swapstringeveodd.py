# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 23:46:36 2019

@author: GRENTOR
"""

string=input()
for i in range(len(string)):
  if (i%2==0):
    print(string[i+1],end='')
  else:
    print(string[i-1],end='')