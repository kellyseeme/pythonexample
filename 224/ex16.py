#!/usr/bin/env python
"""
this is to test the open file ,truncate file,write file and read file
"""
#import the module sys of the fucntion argv
from sys import argv

#get the command line arguments of the script name and the filename
script,filename = argv

#this is print the warning informationm,the truncate is empty the file
#and changge the file content
print "We're going to earase %r." % filename
print "If you don't want that ,hit CTRL-C(`c)."
print "If you do want that,hit RETURN."

#this is get the user input,if use ctrl-c there will be exit the program
raw_input("?")

#open the file of the mode of write
print "Opening the file..."
target = open(filename,"w")

#truncate the file content
print "Truncating the file,Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#get some values to write the file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#wirte the content to the file
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#close the file
print "And finally,we close it."
target.close()
