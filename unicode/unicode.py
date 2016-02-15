#!/usr/bin/env python
# -*- coding:utf-8 -*- 

#use print to print chinese
print u"使用unicode编码"
print u"将unicode转变为uft-8编码".encode("utf-8")

#use raw_input to get the name of chinese
name = raw_input(u"中文".encode("utf-8"))
print name

#write chinese to a file
logFile = open("kel.log","w")
logFile.writelines(u"unicode编码转换成utf-8编码写入".encode("utf-8"))
logFile.close()

#read chinese in a file
readFile = open("kel.log","r")
for line in readFile:
    print line
    print line.decode("utf-8")
readFile.close()
