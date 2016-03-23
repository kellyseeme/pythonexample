#!/usr/bin/env python
#-*coding:utf-8 -*-
#this is use the string method to format the strins
#1.use the ljust is add more space after the string
#2.use the rjust is add more space below the string
#3.use the center is add more space below of after the string

print "|","kel".ljust(20),"|","kel".rjust(20),"|","kel".center(20),"|"

#the string center have more args is the width and the space or other arguments
print "|","kel".center(20,"*"),"|"

print "|","kel".ljust(20,"*"),"|"

print "|","kel".rjust(20,"*"),"|"


"""
用来整理字符串的格式，主要使用的方法为ljust，rjust和center，默认情况下使用空格
第二个参数用来表示用什么字符进行填充
"""
