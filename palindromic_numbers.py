#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:57:29 2020

@author: dskrabacz

Palindromic numbers

"""
import numpy as np
#%%
def flip_number(x):
    string = str(x)
    flipped = string[::-1]
    return int(flipped)

#%%
x = 1

while x<999:
    y = x*flip_number(x)
    if y == flip_number(y):
        print(abs(x-y))
    x +=1
#%%

x=100

while x<999:
    y = 900
    while y<999:
        z = x*y
        y+=1
        if z == flip_number(z):
            print(x,y,z)
    x+=1


#%% Integer split

n = 5368
dummy_list = []
for x in str(n):
    print(x)
    dummy_list.append(int(x))
#%%
"""
Palindromic strings

"""

def checkPalindrome(inputString):
    if inputString[::-1] == inputString:
        return True
    else:
        return False

#%% tester
        
print(checkPalindrome('aabbaa'))

print(checkPalindrome('abbaa'))

print(checkPalindrome('a'))

#%% first duplicate

a = np.array([1,2,3,4,1,2,3,2])

for i in np.arange(len(a)):
    print (a[i])
#def firstDuplicate(a):
    