#!/usr/bin/env python3

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd,[1,2,3,4,5,6]))
print(L)

def not_empty(s):
    return s and s.strip()

L2 = list(filter(not_empty,['jack','is ',None,' ']))
print(L2)
