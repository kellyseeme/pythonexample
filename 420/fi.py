#!/usr/bin/env python
def factoral(n):
    if n == 0 or n == 1:
        return n
    else:
        return n*factoral(n-1)
print factoral(4)
