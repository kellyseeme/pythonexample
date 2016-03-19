#!/usr/bin/env python
"""
this is a class Date,and this is for the static method and class method
"""

#define a class Date
class Date(object):
    day  = 0
    month = 0
    year = 0

#define the init parameter
    def __init__(self,day=0,month=0,year=0):
        self.day = day
        self.month = month
        self.year = year

#this is for the class method ,and the method is use parameter
#this must use the parameter of the self,this is for the object
    def printf(self):
        print "the time is %s %s %s " %(self.day,self.month,self.year)

#this is define a classmethod,and the praemter have a cls,and can use the cls to create a class
#cls is passed of the class,then can initiate the object
    @classmethod
    def from_string(cls,date_as_string):
        day,month,year = map(int,date_as_string.split("-"))
        date1 = cls(day,month,year)
        date1.printf()

#this is the static method,and thre is do something to manage the logic,not the class or object
    @staticmethod
    def is_date_valid(date_as_string):
        day,month,year = map(int,date_as_string.split("-"))
        return day <= 31 and month <= 12 and year <= 3999

#a = Date(2012,12,3)
#a.printf()
Date.from_string("2016-12-1")
is_date = Date.is_date_valid("2011-12-01")
print is_date

