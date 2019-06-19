# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:16:37 2019

@author: GRENTOR
"""
a, b = map(int, input().split())
def prime_check(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               return False
               break
       else:
           return True
    else:
       return False
       
prime_list = list(filter(prime_check,range(a, b)))
print(*prime_list)