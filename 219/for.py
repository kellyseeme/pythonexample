#!/usr/bin/env python
"""this is for test for to strip 

   this is to strip the \n of the list
   first use the enumrate to get the index and value.
   second use the strip to cut the \n
"""
a = [["abc\n","kellyseeme\n"],["kel\n"]]

for k,m in enumerate(a):
    for i,n in enumerate(m):
        print a[k][i].strip()
