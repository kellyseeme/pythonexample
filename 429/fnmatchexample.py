#!/usr/bin/env python

import os
import fnmatch

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename,'*.txt'):
        print filename


if fnmatch.fnmatch('kel','?el'):
    print 'match'

if fnmatch.fnmatch('kel','[a-z]el'):
    print 'match'

if fnmatch.fnmatch('1el','[!a-z]el'):
    print 'match'
