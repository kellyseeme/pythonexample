#!/usr/bin/env python
"""
this test is to use the function meaning.

first we must know how to define a function,use the keywords of def
and there example used two arguments,then how to pass the arguments,used four ways
"""
#this is the function definetion,and the function have two arguments
def cheese_and_crackers(cheese_count,boxes_of_crakers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crakers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#this is we use the arguments passed directly,give two numbers to function use
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)


print "OR,we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#this is to use the variable to the arguments,and it will pass to the functions
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#in the function call,we can do math to pass the arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20,5 + 6)

#there used the function is combing the two variables use math
print "And we can combine the two variables and math:"
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)
