#!/usr/bin/env python
import itertools
class Kel(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return repr((self.name,self.age))
kel = [Kel('kel',25),Kel('jun',32),Kel('no',22),Kel('other',40)]

def get_age(age):
    if age.age < 20:
        return 'small'
    elif age.age < 30:
        return 'middle'
    else:
        return 'old'
kel_list = sorted(kel,key=get_age)
print kel_list
for m,n in itertools.groupby(kel_list,key=get_age):
    print m
    print list(n)
