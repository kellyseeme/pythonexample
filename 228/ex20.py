#!/usr/bin/env python
"""
this is to test the functions and files

use the files to read the files content,and restart and get the content and line number
"""

#this is import the module of sys,get the file name from the sys,argv
from sys import argv

#use the sys.argv get the script name and the input filename
script,input_file = argv

#this is definetion of the function,to read all the file contents,
#and this function argument is a file object
def print_all(f):
    print f.read()

#this is a file object too ,and this is put the pointer to the start of the text
def rewind(f):
    f.seek(0)

#this is get the line of the content,and there have two arguments,first is pass the line  number
#the second is a file object,when is readfile,there will be move in a file object
def print_a_line(line_count,f):
    print line_count,f.readline()
#this is open the file,return a file obejct
current_file = open(input_file)

print "First let's print the whole file:\n"
#call the function to print all the file content
print_all(current_file)

print "Now let's rewind,kind of like a tape"
#this is call the function to get the start of the file
rewind(current_file)

print "Let's print three lines:"
#this is get the firist line of the file content
#and change the line number,so there can all call the function to get the file content
current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1

print_a_line(current_line,current_file)
current_file.close()
