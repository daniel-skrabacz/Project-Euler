#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:48:37 2020

@author: dskrabacz

Smallest multiple

"""
import numpy as np
#%%

primes = [2,3,5,7,11,13,17,19]
x=1
while x<969969000:
    x +=1
    if x%19 == 0 and x%17==0 and x%13 == 0 and x%11==0 and x%7==0 and x%5==0 and x%3 ==0 and x%2==0:
        if x%20 ==0 and x%18==0 and x%16==0 and x%15==0 and x%14==0 :
            print(x)
        
    