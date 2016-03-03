#!/usr/bin/env python

zoo = ("wolf","elephant","penguin")
print "Number of animals inthe zoo is ",len(zoo)

new_zoo = ("monkey","dophin",zoo)
print "Number animals in the new zoo is",len(new_zoo)
print "All animals in the new zoo are",new_zoo
print "Animals broutht from the old zoo are",new_zoo[2]
print "Last animal broutht from old zoo is ",new_zoo[2][2]
