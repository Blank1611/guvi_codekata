# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:25:02 2019

@author: GRENTOR
"""

# Python program to check if the input number is prime or not

num = 1
flag=True
while flag==True:
# prime numbers are greater than 1
    if num > 1:
# check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime number")
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")
    userinput = input('Do you want the next prime number? Yes/No :')
    if userinput.lower()[0] == 'y':
        num += 1
    else:
        flag = False