#!/usr/bin/env python

def fact(x):
    if x == 1:
        return 1
    while x != 1:
        return x*fact(x-1)

print fact(1)
print fact(10)
print fact(5)
