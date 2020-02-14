#!/usr/bin/env python3

L = sorted([26, 5, -1, -5, 1])
print(L)

L = sorted([26, 5, -1, -5, 1], key=abs)
print(L)

L = sorted(['bnob','abb','ttt','iii'], key=str.lower)
print(L)

L = sorted(['bnob','abb','ttt','iii'], key=str.lower, reverse=True)
print(L)

L = [('jack',90),('king',85),('admin',50),('tom',68)]
def by_name(t):
    return t[0]
def by_sorce(t):
    return -t[1]

L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_sorce)
print(L2)
print(L3)
