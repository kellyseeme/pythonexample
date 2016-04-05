#!/usr/bin/env python
import itertools

print 'this is the difference of the imap and map'
itre = itertools.imap(pow,[1,2,3],[1,2,3])
print itre
for i in itre:
    print i
li = map(pow,[1,2,3],[1,2,3])
print li

print 'this is the difference of ifilter and filter'
ifil = itertools.ifilter(lambda x:x >5 ,range(10))
print ifil
for i in ifil:
    print i
ifilfalse = itertools.ifilterfalse(lambda x:x>5,range(10))
print ifilfalse
for i in ifilfalse:
    print i

li = filter(lambda x:x>5,range(10))
print li

print 'this is the other function of itertools'

take = itertools.takewhile(lambda x:x>5,[6,2,6,7,3])
for i in take:
    print 'this is the takewhile function ',i 
drop = itertools.dropwhile(lambda x:x>5,[1,2,6,7,3])
for i in drop:
    print 'this is the dropwhile function ',i 
