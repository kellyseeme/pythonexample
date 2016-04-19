#!/usr/bin/env python
#-*- coding:utf-8 -*-
import tab
name = raw_input("plese input your name:").strip()
age =  int(raw_input("please input your age:"))
sex = raw_input("plese input your sex:").strip()
job = raw_input("plase input your job:")

print '''
	personal info
	NAME: %s
	Age: %s
	Sex:%s
	Job:%s
''' % (name,age,sex,job)

if age >= 28:
    print "your can have a holiday"
elif sex == "F":
    print "your sexy"
else:
    print "your are old lady"
