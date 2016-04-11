#!/sur/bin/env python
#-*- coding:utf-8 -*-
"""
this is a example to get the all branch item of a list or tuple
"""

def list_or_tuple(x):
    'this is to check the is is a list or a tuple'
    return isinstance(x,(list,tuple))
def flatten(sequence,to_expand=list_or_tuple):
    for item in sequence:
        if to_expand(item):
            'this is get the recursion of the item'
            for subitem in flatten(item,to_expand):
                yield subitem
        else:
            yield item

#for the flatten is get a generator,then use the for can get the all value
for x in flatten([1,'kel',[3,['some','others'],4,[5,6],[7,8]]]):
    print x,

def nostring_iterable(obj):
    'this is to check the obj is a iterable and its not a string'
    try:
        iter(obj)
    except TypeError:
        return False
    else:
        return not isinstance(obj,basestring)

print 'string is not iterable'
for x in flatten([1,'kel',[3,['some','others'],4,[5,6],[7,8]]],to_expand=nostring_iterable):
    print x,

def flatten1(sequence,to_expand=list_or_tuple):
    'this is the function of use no recurtion,use the pop and append to get the hightes list item'
    iterators = [iter(sequence)]
    while iterators:
        for item in iterators[-1]:
            if to_expand(item):
                iterators.append(iter(item))
                break
            else:
                yield item
        else:
            iterators.pop()

print 'string is not iterable'
for x in flatten1([1,'kel',[3,['some','others'],4,[5,6],[7,8]]],to_expand=nostring_iterable):
    print x,
