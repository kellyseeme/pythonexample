#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
this file is to concatenate the strings
"""
#this is use join to add the list of string
pieces = ["kel","is","the best"]
print "".join(pieces)

#use for to add string
other = ""
for i in pieces:
    other = other + i

print other

#use %s to change the string
print "%s %s %s"% (pieces[0],pieces[1],pieces[2])

print "kel" + "is" + "the best"

#use function to use the string
import operator
print reduce(operator.add,pieces,"")

"""
在进行拼接字符串的时候，有很多方法，但是都会产生中间变量
最好的方法是使用join方法，在使用join方法的时候，首先构建列表list，然后使用"".join(list)即可，性能最佳
其次的方法是使用%s进行替换，从而在有的是数字的时候，也不需要用str进行字符串的转换
reduce方法用来对sequence的pieces的进行add操作，初始化的值为空，最后返回一个值，对序列中值
进行从左到右的function的operator。add操作
"""
