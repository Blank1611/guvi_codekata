# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:47:46 2019

@author: GRENTOR
"""

a = ['aab', 'xyx']
b = []
f = list(zip(*a))
s = 2*[set(f)]
w1 = set(a[0])
w2 = set(a[1])

print(w1)
print(len(w1))
print(w2)
print(len(w2))
print(s)
print(2*[len(s)])
der = [len(set(a[0])),len(set(a[1]))]
ass =  2 * [len(set(zip(a[0],a[1])))]
print(der)
print(ass)
'''for i in zip(*a):
    b.append(i)'''
