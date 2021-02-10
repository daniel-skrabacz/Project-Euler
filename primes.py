#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:19:07 2020

@author: dskrabacz

Calculating Primes

"""

#%% Find the largest prime factor of a composite number

def maxPrime(n):
    factor = 2
    lastFactor = 1
    while n>1:
        if n%factor == 0:
            lastFactor=factor
            n = n/factor
            while n%factor == 0:
                n=n/factor
        factor = factor + 1
    return lastFactor

# function to check if the number is 
# prime or not 
def isPrime(n) : 
	# Corner cases 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True

	# This is checked so that we can skip 
	# middle five numbers in below loop 
	if (n % 2 == 0 or n % 3 == 0) : 
		return False

	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6

	return True

# print all prime numbers 
# less than equal to N 
def printPrime(n): 
	for i in range(2, n + 1): 
		if isPrime(i): 
			print (i, end =" ") 

n = 7			
printPrime(n) 


#%% 10001st prime number
    
n = 1
some_list = []
while n<2000000:
    n+=1
    if isPrime(n) == True:
        some_list.append(n)