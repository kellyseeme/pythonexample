#!/usr/bin/env python
import itertools

def height_alias(height):
    if height > 180:
        return 'tall'
    elif height < 160:
        return 'short'
    else:
        return 'middle'

persons = [191,159,156,170,177,190,183,185]
sorted(persons,key=height_alias) 

for m,n in itertools.groupby(persons,key=height_alias):
    print m
    print (list(n))
