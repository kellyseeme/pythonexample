#!/usr/bin/env python
'this is the example of print the strings for printf'
import sys
def printf(format,*args):
    'this is defind the function of printf,and use the tuple arguments'
    sys.stdout.write(format % args)

result_tuple = (1,2)
printf('Result tupe is : %s',result_tuple)

def printa(format,**kwds):
    'this is use the dictionay arguments,when use the dictionary arguments ,must use the dictonary with **'
    sys.stdout.write(format % kwds)

d = {'a':'kel'}
printa('Result dictionary is : %r' ,**d)
