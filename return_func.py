#!/usr/bin/env python3

def calc_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax 
    return sum

f = calc_sum(1,2,3,6)
print(f)
print(f())



print('----------------------')
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
