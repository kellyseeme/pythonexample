#!/usr/bin/env python
L = []
n = 1
while n < 99 :
    L.append(n)
    n = n + 2
print L
print [i for i in range(1,100,2)]

print L[:3]
