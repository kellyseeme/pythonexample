#!/usr/bin/env python
"""
this is to check this item is in the list or not
"""
def get_list(li,i,v=None):
    if -len(li) <= i <len(li):
        return li[i]
    else:
        return v

list1 = [1,2,3,'kel']
print get_list(list1,3)
print get_list(list1,8)
