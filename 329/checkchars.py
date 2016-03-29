#!/usr/bin/env python

def containsAny(seq,aset):
    """check the seq is have the aset chars"""
    for c in seq:
        if c in aset: return True
        return False

if __name__ == "__main__":
    if containsAny('abc','kela'):
        print "there have some chars in it"
    else:
        print "there is not hvae"
