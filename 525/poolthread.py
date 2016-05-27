#!/usr/bin/env python

import multiprocessing

def f(n):
    return n*n

p = multiprocessing.Pool(5)
print p.map(f,[1,2,3])
