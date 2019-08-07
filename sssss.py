# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:55:03 2019

@author: GRENTOR
"""

v=["N","NE","E","SE","S","SW","W","NW"]
h=input()
print(v[(v.index(h)+int(int(input())/45))%8])