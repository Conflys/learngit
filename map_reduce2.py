#!/usr/bin/env python3

def normalize(name):
    return name[0].upper() + name[1:].lower()

L = ['admin','jack_King']
L2 = list(map(normalize, L))
print(L2)
