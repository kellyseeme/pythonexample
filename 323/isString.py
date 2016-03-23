#!/usr/bin/env python
#-*- coding:utf-8 -*-
#this is test a string is a string or not

#this is use isinstance to check is this a string
def isString(x):
    return isinstance(x,basestring)


print map(isString,["kel",34,u"ko"])


#this is use the duck string to test a string is a string
def isStringLike(obj):
    try:
        obj.lower() + ""
    except:
        return False
    else:
        return True

print map(isStringLike,["kel",34,u"ko"])

"""
用来检查一个字符串是否是字符串，
第一种方法是用isinstance来进行检查，主要是由于str和unicodestring都是basestring的子类，从而
可以使用isinstance来进行检查
第二种方法是使用鸭子判断法，叫声像鸭子，行为像鸭子，那么就认识是
"""
