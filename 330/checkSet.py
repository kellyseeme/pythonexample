#!/usr/bin/env python
"""
this is using to check chars in another list
"""
#this is use loop to check
def containsAny(seq,aset):
    'seq chars in aset.return True or flase'
    for c in seq:
        if c in aset:
            return True
    return False

import itertools
def containsAnyUsingitertools(seq,aset):
    for item in itertools.ifilter(aset.__contains__,seq):
        return True
    return False

def containsAnyUsingset(seq,aset):
    return bool(set(aset).intersection(seq))

a = "kel"
a_list = ['some','kelasef','kel','k']

if containsAny(a,a_list):
    print "there have some chars"
else:
    print "there is not have"

if containsAnyUsingitertools(a,a_list):
    print "there have some chars"
else:
    print "there is not have"

if containsAnyUsingset(a,a_list):
    print "there have some chars"
else:
    print "there is not have"

def containsOnly(seq,aset):
    'check the seq have the aset item'
    for c in seq:
        if c not in aset:return False
    return True
def containsALL(seq,aset):
    return not set(aset).difference(seq)
