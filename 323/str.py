#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
this is every time process a charamter
"""
#define a character
str = "this"

#use the iteral to process the string,string use for
for i in str:
    print "A is the character %s" % i

#this is use the list compretion,get a list and process it
for i in  ["B is the character %s "% i for i in str]:
    print i

#this is put a string change to a list,then literal the list
liststr = list(str)
for i in liststr:
    print "C is the charaeter %s" % i

#this is define a function to process a charameter
def processCharacter(x):
    print "D is a character %s" % x

#this is use the map to process a character,this is use the map function
map(processCharacter,str)

"""
处理字符串中的每个字符可以使用四中方法：
1、直接使用for循环来遍历字符串
2、使用列表解析来处理字符串中的字符
3、将字符串转换成列表，然后对列表进行处理
4、使用内建的map函数来进行处理
"""
#this is use the set to get the same character for the twon strings
magic_chars = set("sfjsjfopajopfjsofjsj")
poppings_chars=set("fefefsjiosjfsjfsfpokge[pgke[gkehgkekgho")
#use & to get the same character of the two strings
print "".join(magic_chars & poppings_chars)

"""
在最后使用了集合的方式，从而得到两个不重复数据的集合，然后得到两个集合中相同的字符
"""
