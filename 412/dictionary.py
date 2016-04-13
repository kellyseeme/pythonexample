#!/usr/bin/env python
"""
this is the dictionary examples
"""

d = {'data':'kel','name':'kel','age':28}

print d.get('age')
print d.get('some not eixst')
print d.pop('some not exist','not exist')

if 'kel' in d:
    print d['kel']
else:
    print 'there is no this key'

try:
    print d['kel']
except KeyError:
    print 'this key is not exist'

print d.pop('data')
d['some'] = 'otehr'
print d

data = dict(kel='some',some='other')
print data
data ={'kel':'for'}
print data
import time
#this is use function to create a dict
start_time=time.time()
the_keys = [1,2,3,4]
the_values = ['kel','some','other','test']
d = dict(zip(the_keys,the_values))
print d
print time.time()-start_time

import itertools
start_time=time.time()
d = dict(itertools.izip(the_keys,the_values))
print d
print time.time()-start_time

import string
count_by_letter = dict.fromkeys(string.ascii_lowercase,0)
print count_by_letter
count_leeter =dict.fromkeys((1,2,3),'kel')
print count_leeter

#use a list item to create a dictionary
list1 = [1,2,3,4,5]
def dictFromList(keysAndValues):
    return dict(zip(keysAndValues[::2],keysAndValues[1::2]))
print dictFromList(list1)

#this is use a generator the get the list to dict
def pairwise(iterable):
    itnext =iter(iterable).next
    while True:
        yield itnext(),itnext()
def dictFromSequence(seq):
    return dict(pairwise(seq))

d.update(pairwise(('kel','some')))
print d

def sub_dict(somedict,somekeys,default=None):
    return dict([(k,somedict.get(k,default)) for k in somekeys])

def sub_dict_remove(somedict,somekeys,default=None):
    return dict([(k,somedict.pop(k,default)) for k in somekeys])

d = {'a':5,'b':6,'c':7}
print sub_dict(d,'ab'),d
print sub_dict_remove(d,'ab'),d
d = {'a':5,'b':6,'c':7}
print dict(zip(d.itervalues(),d.iterkeys()))
