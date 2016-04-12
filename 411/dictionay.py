#!/usr/bin/env python

d = {'key':'value'}
print d.get('key','not found')
print d.get('kel','kel is not found')

if 'key' in d:
    print d['key']
else:
    print 'not found'

try:
    print d['key']
except KeyError:
    print 'not found'
