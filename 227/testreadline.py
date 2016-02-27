#!/usr/bin/env python
"""
this test fuction is to prove the f.read() is not loop

this can't prove the loop
"""
f = open("kel","r")
while True:
    print f.readline().strip()
    if f.readline() != "":
        print f.readline().strip()
    else:
        break
f.close()
