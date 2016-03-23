#!/usr/bin/env python
#-*- coding:utf-8 -*-
#define a string
x = "   kel   "
#strip is to cut the space of the head and tail
#lstrip is cut the space of the begin
#rstrip is cut the space of the end
print "|",x.strip(),"|",x.lstrip(),"|",x.rstrip(),"|"

#define a string
x = "xyxxyy hejyx yyx"
#if there have a chars ,then the begin and end will cut the chars of the string
print x.strip("xy")

x = "xyyxxykelxyxyyx"
print x.strip("xy")
"""
用来删除开后和结尾的空格，然后获取字符串
lstrip表示删除开头的空格
rstrip表示删除结尾的空格
strip表示删除开头和结尾的空格
当strip里面有参数的时候，那么会删除开头和结尾的字符串中的字符，只删除开头和结尾的，其余的不删除
"""
