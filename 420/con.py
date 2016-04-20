#!/usr/bin/env python

def convert(func,seq):
    return [func(eachNum) for eachNum in seq]

if __name__ == '__main__':
    myseq = (123,45.67,9999L)
    print convert(int,myseq)
