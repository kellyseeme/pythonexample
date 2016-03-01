#!/usr/bin/env python
import math
def my_abs(x):
    if x >= 0:
        return x
    else:
        return abs(x)

def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny

kel = move(4,4,2)
print kel
