#!/usr/bin/env python

"""
not my solution

I feel like this solution has something to do with Euclid's algorithm for
finding the GCD
"""

with open("s5.in", 'r') as infile:
    number = int(infile.readline().strip())
 
cost = 0

def find_smallest_factor(number):
    max_factor = int(number**0.5) + 1 #largest number we need to go to before concluding number is prime
    if number % 2 == 0: return 2
    for factor in range(3, max_factor, 2): 
        if number % factor == 0:  return factor

while number != 1: # 1 is what we're trying to get to
    factor = find_smallest_factor(number)
    if factor:
        leftover = number / factor #everything that is left after the smallest factor is divided out
        number -= leftover #number can be reduced by this because 
        cost += number / leftover
    else: # if number is prime, go back only 1
        number -= 1
        cost += number
    print number, factor, cost
        
print cost