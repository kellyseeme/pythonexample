#!/usr/bin/env python
"""
this is for some practice of the string and function and the list or tuple,and the newline in escapes
"""
#use print to print some strings
print "Let's practice everything."
#there is print the special characters of the escapes,use escape then there some best formula
print "You \'d need to know \' bout eacapes with \\ that do \n newlines and \t tabs."

#this is use the """to print more form,then we will control the form
poem = """
\t The lovely world
with logic so firmly planted
cannot comprehend passion from intuition
and requires an explanation
\n\t where there is none.
"""

print "--------------"
print poem
print "--------------"

#this is to the math
five = 10 -2 +3 -6
#print the math result,and print it use formula
print "this should be five :%s "% five

#define a function,then return some values
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans /1000
    crates = jars /100
    return jelly_beans,jars,crates
#this is to call the functions,and get the returns use the vars
start_point = 10000
beans,jars,crates = secret_formula(start_point)

print "With a starting point of :%d" % start_point
#we can also use the functions when formulate the parameters to get the values
print "We'd have %d beans,%d jars,and %d ceates." % (beans,jars,crates)

#when the part of function works,inside the function the varisble is tempory,when your return the value
#then you can use it to assigned to a variable
start_point = start_point /10

print "We can also dothat this way:"
print "We'd hvae %d beans,%d jars,and %d crates." % secret_formula(start_point)
