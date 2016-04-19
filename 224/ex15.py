#!/usr/bin/env python 
"""
this is to test the open file and read the file content.
use the two way go get the filename :
	1.get the name from the sys.argv in the command line
	2.get the name from the user keyboard,is the user input
there have open a file ,and using the file object of attribute read to
read the file content
"""
#import the module of sys and the attribute argv
from sys import argv
#get the script name and the filename
script,filename =argv

#open the file
txt = open(filename)

#print the filename and print the file content using file.read()
print "Here's your file %r:" % filename
print txt.read()

#get the filename from the raw_input ,is user input
print "Type the filename again:"
file_again = raw_input(">>")

#open the file again,and read the file content
txt_again = open(file_again)
print txt_again.read()
