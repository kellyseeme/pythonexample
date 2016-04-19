#!/usr/bin/env python
#-*- coding:utf-8 -*-
CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = u'中文\n'
bytes_out = hello_out.encode(CODEC)
f = open(FILE,'w')
f.write(bytes_out)
f.close()

f = open(FILE)
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print hello_in,
