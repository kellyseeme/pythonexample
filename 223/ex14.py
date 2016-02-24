#!/usr/bin/env python
"""
this is to use argv and raw_input

the argv is in the command line,then can use the module of sys ,get the value for argv
the raw_input is to get the keyboard values,for the user input
there define the prompt ,then not to type it again and again
in the \""" there can be format and the style
"""
from sys import argv

script,user_name,age = argv
prompt = ">>>"

print "Hi %s,Y'm the %s script." % (user_name,script)
print "Your age is %r" %age
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "where do you live? %s." % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright ,so you said %r about liking me.
Your age is %r.
You live in %r.Not sure where it is.
And you have a %r computer,Nice.
""" % (likes,age,lives,computer)
