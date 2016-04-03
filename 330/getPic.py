#!/usr/bin/env python
"""
imap(function,iter1,iter2)-->function(iter1,iter2),if one iter is no get the item,then will be stop
ifilter(predicate,iterable)-->predicate(item) is True's item
"""
import itertools
def anyTrue(function,seq):
    return True in itertools.imap(function,seq)
def endsWith(s,*endings):
    return anyTrue(s.endswith,endings)

import os
for filename in os.listdir('.'):
    if endsWith(filename,'.jpg','.gif','.jpeg','.log'):
        print filename

