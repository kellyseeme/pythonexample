#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
this is a unicode file test
"""
#this is the code use utf-8
CODEC = 'utf-8'
FILE = 'unicode.txt'

#this is write the content to the file,then must be encode to the utf-8
hello_out = u'Hello KEL,中文测试\n'
bytes_out = hello_out.encode('utf-8')
f = open(FILE,'w')
f.write(bytes_out)
f.close()

#this is read from the file,then must decode the file
f = open(FILE,'r')
hello_in = f.read()
bytes_in = hello_in.decode(CODEC)
f.close()
print bytes_in,
