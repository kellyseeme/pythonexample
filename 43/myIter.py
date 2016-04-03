#!/usr/bin/env python
"""
this is for a example of set the iterable and iterator
"""
#this is define a class of Data,this is a iterable
class Data(object):
#this is the __init__ function,get the values of the more arguments,then pass it to get a tuple
    def __init__(self,*args):
        self.data = tuple(args)
#this is a itre funtion to retuan a Iterator,and pass the initionlization of a data()
    def __iter__(self):
        return DataIterable(self)

#this is the class of Iterator
class DataIterable(object):
#this is the initionlization function,get the pass data attribute of data,and have another attribute of index
    def __init__(self,data):
        self.data = data.data
        self.index = 0
#this is the method of __iter__funtion,then it will be iterable
    def __iter__(self):
        return self
#this is the method of next,then it must be a iterator,and can get the stopiteration of exception
    def next(self):
        if self.index == len(self.data):
            raise StopIteration
        else:
#this is get the next value of the iterator
            data = self.data[self.index]
            self.index += 1
            return data
if __name__ == '__main__':
#for this the iterable ,then it will be loop more times,but the iterator only loop one time
    data = Data(1,'kel','xyz',4.56)
    for values in data:
        print values
    for values in data:
        print values
