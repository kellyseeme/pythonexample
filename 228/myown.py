#!/usr/bin/env python
"""
this is for the test of funtion call
there have more ways call the function

"""
import sys

def myfunction(arg1):
    print arg1

myfunction("this is directly use")

kel = "this is for variables"

myfunction(kel)

myfunction("this is "+ "combing the string in the arguments")

myfunction(raw_input("this is the user input >>"))

myfunction("this is for the command line"+ sys.argv[0])


if __name__  == "__main__":
   myfunction("this is for the script name")

